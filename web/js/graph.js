import {CanvasData} from './canvas_data.js';
import {CoordinateSystemCanvas} from './coordinate_system_canvas.js';
import {GraphCanvas} from './function_graph_canvas.js';

const GRID_COLOR = '#757575';
const AXIS_COLOR = 'white';
const GLOBAL_SCALE = 1;
const MAX_LINE_WIDTH = 1;
const X_RANGE_ERROR = 'Error: the minimum value of the function range is greater than the maximum';
const Y_RANGE_ERROR = 'Error: the minimum value of the function domain is greater than the maximum';

export class Graph {
    constructor() {
        this.GRAPH_MIN_WIDTH = 1000;
        this.GRAPH_MIN_HEIGHT = 750;

        this.functionEntry = document.querySelector('.function-entry');
        this.colorPalette = document.querySelector('.color-palette');
        this.container = document.querySelector('.graph');
        this.applyButton = document.querySelector('#draw');
        this.clearButton = document.querySelector('#clear');
        this.posX = document.querySelector('.pos-x');
        this.negX = document.querySelector('.neg-x');
        this.posY = document.querySelector('.pos-y');
        this.negY = document.querySelector('.neg-y');

        this.canvasData = new CanvasData(GLOBAL_SCALE, 10, -10, 10, -10);
        this.coordinateSystem = new CoordinateSystemCanvas(this.canvasData, MAX_LINE_WIDTH, GRID_COLOR, AXIS_COLOR);
        this.graphCanvas = new GraphCanvas(MAX_LINE_WIDTH * 2, this.canvasData);

        this.width = this.GRAPH_MIN_WIDTH;
        this.height = this.GRAPH_MIN_HEIGHT;

        this.canvasData.canvasContainer.onmousemove = (event) => {
            this.coordinateSystem.drawMouseTrack(event.x, event.y);
        };
        this.canvasData.canvasContainer.onmouseout = () => {
            this.coordinateSystem.resize();
        };
        this.applyButton.onclick = () => { this.apply(); };
        this.clearButton.onclick = () => { this.clear(); };
    }

    enable() {
        this.container.style.display = 'flex';
    }

    disable() {
        this.container.style.display = 'none';
    }

    async apply() {
        const posX = +this.posX.value;
        const negX = +this.negX.value;
        const posY = +this.posY.value;
        const negY = +this.negY.value;

        if (negX >= posX) {
            showErrorMessage(X_RANGE_ERROR);
            return;
        } else if (negY >= posY) {
            showErrorMessage(Y_RANGE_ERROR);
            return;
        }
        this.canvasData.startPosX = posX;
        this.canvasData.startNegX = negX;
        this.canvasData.startPosY = posY;
        this.canvasData.startNegY = negY;


        this.canvasData.globalScaleX = 1;
        this.canvasData.globalScaleY = 1;

        this.canvasData.init();
        this.coordinateSystem.resize();

        const inputData = this.functionEntry.value;
        const colorData = this.colorPalette.value;
        if (!inputData) {
            return;
        }
        this.graphCanvas.clear();
        await this.graphCanvas.updateParameters(inputData, colorData);
        this.graphCanvas.drawGraph();
    }

    clear() {
        this.functionEntry.value = '';
        this.graphCanvas.clear();
    }

    resize_canvas() {
        this.coordinateSystem.resize();
        this.graphCanvas.resize();
    }
}
