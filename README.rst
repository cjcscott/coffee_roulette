===============
coffee_roulette
===============


.. image:: https://img.shields.io/pypi/v/coffee_roulette.svg
        :target: https://pypi.python.org/pypi/coffee_roulette

.. image:: https://img.shields.io/travis/cjcscott/coffee_roulette.svg
        :target: https://travis-ci.com/cjcscott/coffee_roulette

.. image:: https://readthedocs.org/projects/coffee-roulette/badge/?version=latest
        :target: https://coffee-roulette.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status



A quick program to generate randomly split up a list of people for small group tasks. For example

.. code-block:: bash

    $ coffee_roulette alice bob carl dana engelbert francesca gerald --minsize 2 --maxsize 3
    Determined splitting:
    ['dana' 'francesca']
    ['engelbert' 'gerald']
    ['alice' 'bob' 'carl']

* Free software: GNU General Public License v3
* Documentation: https://coffee-roulette.readthedocs.io.


Features
--------

* Given a list of people, generates random partitioning of them into small groups.
* The maximum and minimum sizes of groups, as well as whether to try to maximise or minimise group sizes, can be adjusted.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
