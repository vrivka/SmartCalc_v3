export class Canvas {
    constructor(canvasData) {
        this.canvas = document.createElement('canvas');
        this.ctx = this.canvas.getContext('2d');
        this.canvasData = canvasData;
        this.canvas.width = this.canvasData.width;
        this.canvas.height = this.canvasData.height;
    }

    drawLine(width, color, x0, y0, x1, y1) {
        this.ctx.beginPath();
        this.ctx.lineWidth = width;
        this.ctx.strokeStyle = color;
        y0 = y0 < 0 ? 0 : y0;
        y1 = y1 < 0 ? 0 : y1;
        y0 = y0 > this.canvasData.height ? this.canvasData.height : y0;
        y1 = y1 > this.canvasData.height ? this.canvasData.height : y1;

        this.ctx.moveTo(x0, y0);
        this.ctx.lineTo(x1, y1);
        this.ctx.stroke();
    }

    get width() {
        return this.canvas.width;
    }

    get height() {
        return this.canvas.height;
    }

    resize() {
        this.canvas.width = this.canvasData.width;
        this.canvas.height = this.canvasData.height;
        this.canvasData.resize();
        this.clear()
    }

    clear() {
        this.ctx.clearRect(0, 0, this.width, this.height);
    }
}