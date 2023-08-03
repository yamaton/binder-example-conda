# Run `jupyter server --generate-config`

# mypy: ignore-errors
c = get_config() # noqa: F821  # pyright: ignore[reportUndefinedVariable]

# jupyter-fs configs
c.SingleUserNotebookApp.root_dir = "work"
c.ServerApp.root_dir = "work"

# Enable deleting non-empty directories
c.FileContentsManager.always_delete_dir = True
