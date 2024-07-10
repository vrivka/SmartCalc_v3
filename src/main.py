import eel
from calc_view import CalcView
import sys
import io
import utils

buffer = io.StringIO()
sys.stdout = sys.stderr = buffer


def on_exit(_, websockets):
    global viewModel
    viewModel.presenter.save_history()
    exceptions = buffer.getvalue()
    if not websockets:
        if exceptions:
            with open(utils.get_resource('exceptions.txt'), 'w', encoding='utf-8') as of:
                of.write(exceptions)
    sys.exit()


if __name__ == '__main__':
    viewModel = CalcView()
    eel.init('web')
    eel.start('index.html', mode="chrome", size=(
        550, 750), close_callback=on_exit, port=0)
