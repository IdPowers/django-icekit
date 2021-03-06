# Changelog

## Next release

  * ICEkit gets a facelift. Content editing now looks cleaner and easier to
    scan. Reordering items is animated, meaning it's easier to keep track of
    what got moved.

  * Improved Image controls, optionally including a title in the caption.

  * `alt_text` is no longer required - some images don't provide content that
    is useful to users who can't see them, though the `alt=` attribute is still
    always included in HTML.

  * Fix a bug where looking for help_text in a placeholder slot that had no
    manual configuration raised a 500, resulting in no layout data found


## 0.14 (20 September 2016)

  * Update the recommended method of running projects via `Docker` and `go.sh`
    to provide a more consistent and familiar experience for developers.

    Old:

        $ docker-compose up                         # Run all services and log to stdout (no interactivity)
        $ docker-compose exec django entrypoint.sh  # Shell into running `django` container to run interactive processes

    New:

        $ docker-compose run --rm --service-ports django  # Start dependant services and shell into a new `django` container

    The benefits are that:

     1. We start with an interactive terminal in which we can any number of
        interactive processes in a familiar way.

     2. It's much easier and quicker to stop and restart the main process (e.g.
        the Django dev server) without having to stop and restart dependant
        services.

     3. We aren't overwhelmed by several screens of log output from all the
        service dependencies.

     4. We don't start a WSGI process in a non-interactive `django` service,
        then have to shell into the container to stop it and replace it with
        an interactive one.

  * Use different locations for `PYTHONUSERBASE` (via Docker) and virtualenv
    (via `go.sh`) directories, to avoid conflicts.

  * Isolate the `go.sh` BASH shell from user's personal `.bashrc` and
    `.profile` files to avoid conflicts and unexpected behaviour.

  * Validate that manually installed dependencies are available when run via
    `go.sh`, and fail loudly.

  * Call `setup-django.sh` by default when `go.sh` is called without arguments,
    to mimic `docker-compose run ... django` default behaviour.

  * Improve the `runtests.sh` script:

     1. Use a database name derived from project directory and Git branch.

     2. Restore `test_initial_data.sql` instead of `initial_data.sql` before
        running tests, so `initial_data.sql` can be used for development.

     3. Only run and report on project tests when run in a project context.

  * Improve detection of `*.sql` file vs source database to restore when
    creating a database.

  * Don't clobber the version of ICEkit installed into the base Docker image
    when building a project image.

  * Avoid failing test builds when Coveralls fails to push its update.

  * Add an authors app.

  * You can now define `help_text` for a fluent placeholder in
    `FLUENT_CONTENTS_PLACEHOLDER_CONFIG`.

  * Improved `ICEkitURLField`, which uses correct `Page` queryset.

Backwards incompatible changes:

  * The default command for `django` service now starts an interactive shell
    instead of `supervisord.sh` (which starts Nginx and Gunicorn). Use the new
    `docker-compose run --rm --service-ports django` command to shell into a
    new `django` container and then manually call `runserver.sh` or
    `supervisord.sh` instead of `docker-compose up`.

  * The `entrypoint.sh` script is now executed via the `ENTRYPOINT` instruction
    in `Dockerfile`. You don't need to explicitly include it as an argument to
    `docker-compose run ...` commands or in `docker-compose.yml` services.

  * Move Node modules and Bower components out of `icekit` package and into
    project template for simplicity and greater visibility. Add ICEkit
    dependencies to your project `bower.json` and `package.json` files.

  * Remove `django-supervisor`. We are now using Supervisor directly because
    it uses a lot of memory and is slow to invoke the whole Django machinery
    just to render a `supervisord.conf` template before starting Supervisor.

    Define additional services in `docker-compose.yml` and a Supervisor config
    file (referenced by the `SUPERVISORD_CONFIG_INCLUDE` environment variable)
    or shell scripts to run additional processes interactively.

## 0.13.1 (14 September 2016)

  * Refactored templates so as to only use bootstrap markup when layout is
    intrinsic. Improved markup for some, particularly quote and OEmbed.

  * Added instructions covering uninstalling a docker project.

  * Installation improvements.

  * Thumbnail configuration should now be specified in settings, not templates.

## 0.12 (30 August 2016)

  * Make project run more consistently without Docker (via `go.sh`).

  * Refactor docs to provide better onboarding.

  * Fix intermittent cache related test failures.

## 0.11 (29 August 2016)

  * Serve Django with Nginx/Gunicorn under Supervisord, to buffer requests,
    facilitate large file uploads (500MB), and take full advantage of multiple
    CPU cores.

  * The `SITE_PORT` setting now represents the public port that the site is
    listening on (Nginx), not the WSGI process (Gunicorn).

  * Use `initial_data.sql` dump to bypass old migrations on first run, not only
    when running tests.

  * Use wrapper scripts for program commands, so we can run programs
    consistently in Docker containers of via Supervisord when not using Docker.

  * Expose private ports (e.g. Gunicorn, PostgreSQL, Redis) to the host on a
    dynamic port during development.

  * Update the `Site` object matching the `SITE_ID` setting in a post-migrate
    signal handler with the `SITE_DOMAIN`, `SITE_PORT` and `SITE_NAME`
    settings.

  * Run celery programs via Supervisord when not using Docker.

  * Configure Docker and non-Docker environments to be more similar so we can
    use more of the same scripts to run.

  * Don't use Redis lock to avoid parallel setup when not using Docker, on a
    single server.

## 0.10.2 (25 August 2016)

  * Run tests in a Docker image on Travis CI and push to Docker Hub on success.
  * Test the same settings module in Docker and Tox.
  * Fix broken tests.

## 0.10.1 (24 August 2016)

  * Speed up tests by restoring a database with migrations already applied.
  * Fix broken tests.

## 0.10 (23 August 2016)

New:

  * [#3](https://github.com/ic-labs/django-icekit/pull/3)
    Include a Django project with ICEkit, making it easier to run in
    development, need less boilerplate code, be less likely to diverge over
    time, and easier to keep up-to-date.

  * [#4](https://github.com/ic-labs/django-icekit/pull/4)
    Make content plugins "portable", making it easier to fork and customise
    them for a project.

Backwards incompatible changes:

  * Make content plugins [portable](topics/portable-apps.md). You will need to
    run an SQL statement for each plugin manually to fix Django's migration
    history when upgrading an existing project.

        UPDATE django_migrations SET app='icekit_plugins_brightcove' WHERE app='brightcove';
        UPDATE django_migrations SET app='icekit_plugins_child_pages' WHERE app='child_pages';
        UPDATE django_migrations SET app='icekit_plugins_faq' WHERE app='faq';
        UPDATE django_migrations SET app='icekit_plugins_file' WHERE app='file';
        UPDATE django_migrations SET app='icekit_plugins_horizontal_rule' WHERE app='horizontal_rule';
        UPDATE django_migrations SET app='icekit_plugins_image' WHERE app='image';
        UPDATE django_migrations SET app='icekit_plugins_instagram_embed' WHERE app='instagram_embed';
        UPDATE django_migrations SET app='icekit_plugins_map' WHERE app='map';
        UPDATE django_migrations SET app='icekit_plugins_map_with_text' WHERE app='map_with_text';
        UPDATE django_migrations SET app='icekit_plugins_oembed_with_caption' WHERE app='oembed_with_caption';
        UPDATE django_migrations SET app='icekit_plugins_page_anchor' WHERE app='page_anchor';
        UPDATE django_migrations SET app='icekit_plugins_page_anchor_list' WHERE app='page_anchor_list';
        UPDATE django_migrations SET app='icekit_plugins_quote' WHERE app='quote';
        UPDATE django_migrations SET app='icekit_plugins_reusable_form' WHERE app='reusable_form';
        UPDATE django_migrations SET app='icekit_plugins_slideshow' WHERE app='slideshow';
        UPDATE django_migrations SET app='icekit_plugins_twitter_embed' WHERE app='twitter_embed';

## 0.9 (11 August 2016)

  * Initial release.
