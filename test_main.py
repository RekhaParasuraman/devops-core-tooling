from main import main


def test_main_prints_welcome_message(capsys):
    main()

    captured = capsys.readouterr()

    assert captured.out == "Welcome to DevOps Core Tooling!\n"
