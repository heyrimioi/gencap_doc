Core objects
==============

.. autoclass:: gencap.Cohort
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: gencap.Pipeline
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: gencap.Task
    :members:
    :undoc-members:
    :show-inheritance:

Global managers
==============

.. py:data:: gencap.task_manager
    :type: gencap.globals.task_manager.TaskRegistry

    Global instance of :class:`gencap.globals.task_manager.TaskRegistry`.

    This is the recommended entry point for managing tasks.  
    See :class:`gencap.globals.task_manager.TaskRegistry` below for available methods.

.. autoclass:: gencap.globals.task_manager.TaskRegistry
    :members:
    :undoc-members:
    :show-inheritance:
    :noindex:
    :exclude-members: _registry, _grouped_registry

.. py:data:: gencap.pipeline_manager
    :type: gencap.globals.pipeline_registry.PipelineRegistry

    Global instance of :class:`gencap.globals.pipeline_registry.PipelineRegistry`.

.. autoclass:: gencap.globals.pipeline_registry.PipelineRegistry
    :members:
    :undoc-members:
    :show-inheritance:
    :noindex:

.. py:data:: gencap.default_pathname_policy_manager
    :type: gencap.globals.path_manager.PathnamePolicyRegistry

    Global instance of :class:`gencap.globals.path_manager.PathnamePolicyRegistry`.

.. autoclass:: gencap.globals.path_manager.PathnamePolicyRegistry
    :members:
    :undoc-members:
    :show-inheritance:
    :noindex:

Project Builder
==============

.. autoclass:: gencap.ProjectBuilder
    :members:
    :undoc-members:
    :show-inheritance:

Utilities
==============

.. autoclass:: gencap.add_module
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: gencap.auto_import_from
    :members:
    :undoc-members:
    :show-inheritance:

.. toctree::
   :maxdepth: 3
   :caption: Others

   gencap.utils