from taskcli.cli import main
from taskcli.storage import TaskStore


def test_add_and_load(tmp_path):
    store = TaskStore(tmp_path / "tasks.json")
    store.add("Write tests")
    store.add("Ship it")
    tasks = store.load()
    assert [t["id"] for t in tasks] == [1, 2]
    assert tasks[0]["title"] == "Write tests"


def test_complete_and_delete(tmp_path):
    store = TaskStore(tmp_path / "tasks.json")
    store.add("A")
    assert store.complete(1) is True
    assert store.load()[0]["done"] is True
    assert store.delete(1) is True
    assert store.load() == []
    assert store.complete(99) is False


def test_cli_list(tmp_path, capsys):
    store = TaskStore(tmp_path / "tasks.json")
    main(["add", "Hello"], store=store)
    main(["list"], store=store)
    out = capsys.readouterr().out
    assert "Hello" in out
