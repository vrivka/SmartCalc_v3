import {Canvas} from "./canvas.js";

export class GraphCanvas extends Canvas {
    inputData = '';
    data = [];
    color = 'black';

    constructor(lineWidth, canvasData) {
        super(canvasData);
        this.canvas.style = "z-index: 1; position: absolute;";
        this.lineWidth = lineWidth;
        this.canvasData.canvasContainer.appendChild(this.canvas);
    }

    drawGraph() {
        let prevX;
        let prevY;
        let currX;
        let currY;
        let scaleX = this.canvasData.gridPixelSizeX / this.canvasData.globalScaleX;
        let scaleY = this.canvasData.gridPixelSizeY / this.canvasData.globalScaleY;

        for (let i = 0; i < this.data.length; i++) {
            let xy = this.data[i];
            if (xy === '+') {
                currY = 0;
            }
            else if (xy === '-') {
                currY = this.canvasData.height;
            }
            else {
                let x = xy[0];
                let y = xy[1];
                currX = x * scaleX + this.canvasData.centerX;
                currY = (-y) * scaleY + this.canvasData.centerY;
            }
            if (i === 0) {
                prevX = currX;
                prevY = currY;
            }
            this.drawLine(this.lineWidth, this.color, prevX, prevY, currX, currY);
            if (xy === '+') {
                prevY = this.canvasData.height;
            }
            else if (xy === '-') {
                prevY = 0;
            }
            else {
                prevX = currX;
                prevY = currY;
            }
        }
    }

    async updateParameters(inputData, colorData) {
        this.inputData = inputData ? inputData : this.inputData;
        this.data = await eel.graph_data(this.inputData, this.canvasData)();
        this.color = colorData ? colorData : this.color;
    }

    async resize() {
        super.resize();
        await this.updateParameters();
        this.drawGraph();
    }
}