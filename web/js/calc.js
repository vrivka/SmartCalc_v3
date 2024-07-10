export class Calc {
    constructor() {
        this.CALC_MIN_WIDTH = 550;
        this.CALC_MIN_HEIGHT = 750;

        this.entry = document.querySelector('.entry p');
        this.container = document.querySelector('.calc');
        this.buttons = document.querySelector('.calc-buttons');
        this.keyboard = this.buttons.querySelectorAll('.btn');
        this.history = document.querySelector('.history');
        this.clearHistory = document.querySelector('.history-clear');
        this.buttonHistory = document.querySelector('#history');
        this.buttonClearHistory = document.querySelector('#clear-history');

        this.calcWidth = 550;
        this.calcHeight = 750;
        this.isHist = false;

        this.buttonHistory.onclick = () => {
            if (!this.isHist) {
                this.buttonHistory.innerHTML = '<img src="./images/calculator_icon.svg" id="hist-icon">';
                this.buttons.style.display = 'none';
                this.history.style.display = 'flex';
                this.clearHistory.style.display = 'flex';
                this.isHist = true;
                this.getHistory();
            } else {
                this.buttonHistory.innerHTML = '<img src="./images/history_icon.svg" id="hist-icon">';
                this.history.style.display = 'none';
                this.clearHistory.style.display = 'none';
                this.buttons.style.display = 'flex';
                this.isHist = false;
                this.offHistory();
            }
        };

        this.buttonClearHistory.onclick = async () => {
            await eel.clear_history();
            this.offHistory();
        };

        this.keyboard.forEach((value) => {
            value.onclick = async () => {
                await eel.keyboard_handler(value.id);
            };
        });
    }

    async keyboard_action() {
        if (!this.isHist) {
            await eel.keyboard_handler(event.key);
        }
    }

    enable() {
        this.container.style.display = 'flex';
    }

    disable() {
        this.container.style.display = 'none';
    }

    setEntry(str) {
        this.entry.innerHTML = str;
    }

    createHistoryComponent(id, expr, res) {
        const component = document.createElement('div');
        component.className = 'history-component';
    
        const buttons = document.createElement('div');
        buttons.className = 'load-buttons';
    
        const exprButton = document.createElement('div');
        exprButton.className = 'btn';
        exprButton.id = `expr-${id}`;
        exprButton.title = 'Load expression';
        exprButton.innerHTML = '<img src="./images/upload_icon.svg">';
    
        exprButton.onclick = () => {
            eel.load_from_history(exprButton.id);
        };
    
        const resButton = document.createElement('div');
        resButton.className = 'btn';
        resButton.id = `res-${id}`;
        resButton.title = 'Load result';
        resButton.innerHTML = '<img src="./images/upload_icon.svg">';
    
        resButton.onclick = () => {
            eel.load_from_history(resButton.id);
        };
    
        const discription = document.createElement('div');
        discription.className = 'history-discription';
    
        const exprElement = document.createElement('div');
        exprElement.className = 'expr';
        exprElement.innerHTML = expr;
    
        const resElement = document.createElement('div');
        resElement.className = 'res';
        resElement.innerHTML = res;
    
        discription.appendChild(exprElement);
        discription.appendChild(resElement);
        buttons.appendChild(exprButton);
        buttons.appendChild(resButton);
    
        component.appendChild(buttons);
        component.appendChild(discription);
    
        this.history.appendChild(component);
    }
    
    async getHistory() {
        const history = await eel.get_history()();
    
        history.forEach((hist) => {
            this.createHistoryComponent(hist['id'], hist['expr'], hist['res']);
        });
    }
    
    offHistory() {
        this.history.innerHTML = '';
    }
}