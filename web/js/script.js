import {Graph} from './graph.js';
import {Calc} from './calc.js';

const calcTabElement = document.querySelector('#calc');
const graphTabElement = document.querySelector('#graph');
const errorContainer = document.querySelector('.error');
const errorMessage = document.querySelector('.error-message');
const errorCloseButton = document.querySelector('#error-close');
const helpButton = document.querySelector('#help');
const helpClose = document.querySelector('#help-close');

const graph = new Graph();
const calc = new Calc();
let minWidth = calc.CALC_MIN_WIDTH;
let minHeight = calc.CALC_MIN_HEIGHT;
let status = 'calc';
let prevStatus = status;

window.onresize = () => {
    if (window.outerWidth < minWidth) {
        window.resizeTo(minWidth, window.outerHeight);
    }
    if (window.outerHeight < minHeight) {
        window.resizeTo(window.outerWidth, minHeight);
    }
    if (status === 'graph') {
        graph.resize_canvas();
    }
};

calcTabElement.onclick = () => {
    graph.width = window.outerWidth;
    graph.height = window.outerHeight;
    minWidth = calc.CALC_MIN_WIDTH;
    minHeight = calc.CALC_MIN_HEIGHT;
    window.resizeTo(calc.width, calc.height);

    calc.enable();
    calcTabElement.style.filter = 'invert(0%)';
    status = 'calc';

    graph.disable();
    graphTabElement.style.filter = 'invert(100%)';
};

graphTabElement.onclick = () => {
    graph.enable();
    graphTabElement.style.filter = 'invert(0%)';
    status = 'graph';

    calc.disable();
    calcTabElement.style.filter = 'invert(100%)';

    calc.width = window.outerWidth;
    calc.height = window.outerHeight;
    minWidth = graph.GRAPH_MIN_WIDTH;
    minHeight = graph.GRAPH_MIN_HEIGHT;
    window.resizeTo(graph.width, graph.height);

    graph.canvasData.init();
    graph.resize_canvas();
};

helpButton.onclick = () => {
    document.querySelector('.help').style.display = 'flex';
    prevStatus = status;
    status = 'help';
};

helpClose.onclick = () => {
    document.querySelector('.help').style.display = 'none';
    status = prevStatus;
};

errorCloseButton.onclick = () => {
    errorContainer.style.display = 'none';
    errorMessage.innerText = '';
    status = prevStatus;
};

document.addEventListener('keydown', async (event) => {
    if (status === 'calc') {
        calc.keyboard_action();
    } else if (status === 'graph') {
        if (event.key === 'Enter') {
            graph.apply();
        } else if (event.key === 'Delete') {
            graph.clear();
        }
    }
});

document.oncontextmenu = () => {
    return false;
};

eel.expose(setEntry);
eel.expose(showErrorMessage);

function setEntry(str) {
    calc.setEntry(str);
}

function showErrorMessage(msg) {
    errorContainer.style.display = 'flex';
    errorMessage.textContent = msg;
    prevStatus = status;
    status = 'error';
}
