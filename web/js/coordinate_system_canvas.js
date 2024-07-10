import { Canvas } from "./canvas.js";

export class CoordinateSystemCanvas extends Canvas {
    constructor(canvasData, maxLineWidth, gridColor, axisColor) {
        super(canvasData);
        this.canvas.id = 'graph-cnv-main';
        this.canvas.style = 'z-index: 0; position: absolute;';
        this.maxLineWidth = maxLineWidth;
        this.gridColor = gridColor;
        this.axisColor = axisColor;
        this.resize();
        this.canvasData.canvasContainer.appendChild(this.canvas);
    }

    drawSystem() {
        /* draw axis */
        this.ctx.beginPath();
        this.ctx.lineWidth = this.maxLineWidth;
        this.ctx.strokeStyle = this.axisColor;
        this.ctx.moveTo(0, this.height);
        this.ctx.lineTo(this.width, this.height);
        this.ctx.moveTo(0, this.height);
        this.ctx.lineTo(0, 0);
        this.ctx.stroke();

        this.ctx.fillStyle = this.axisColor;
        this.ctx.font = '30pt monospace';
        this.ctx.textAlign = 'left';
        this.ctx.textBaseline = 'top';
        this.ctx.fillText('y', 30, 0);
        this.ctx.textAlign = 'right';
        this.ctx.textBaseline = 'bottom';
        this.ctx.fillText('x', this.width - 10, this.height - 35);
        this.ctx.stroke();

        this.ctx.fillStyle = this.axisColor;
        this.ctx.font = '12pt monospace';

        /* draw X axis */
        let stepX = this.canvasData.gridPixelSizeX;

        this.ctx.textAlign = 'center';
        this.ctx.textBaseline = 'bottom';
        for (let x = stepX - 1, i = this.canvasData.neg_x; x < this.width - 2; x += stepX, i += this.canvasData.globalScaleX) {
            this.drawLine(this.maxLineWidth / 3 * 2, this.gridColor, x, 0, x, this.height);
            if (i === 0) {
                this.drawLine(this.maxLineWidth / 3, this.axisColor, x, 0, x, this.height);
            }
            this.drawLine(this.maxLineWidth, this.axisColor, x, this.height, x, this.height - 10);
            this.ctx.fillText(`${i}`, x, this.height - 10);
        }
        this.ctx.stroke();

        /* draw Y axis */
        let stepY = this.canvasData.gridPixelSizeY;

        this.ctx.textAlign = 'left';
        this.ctx.textBaseline = 'top';
        for (let y = this.height - stepY + 1, i = this.canvasData.neg_y; y > 2; y -= stepY, i += this.canvasData.globalScaleY) {

            this.drawLine(this.maxLineWidth / 3 * 2, this.gridColor, 0, y, this.width, y);
            if (i === 0) {
                this.drawLine(this.maxLineWidth / 3, this.axisColor, 0, y, this.width, y);
            }
            this.drawLine(this.maxLineWidth, this.axisColor, 0, y, 10, y);
            this.ctx.fillText(`${i}`, 10, y);
        }
        this.ctx.stroke();

        /* scale draw */
        this.ctx.fillStyle = this.axisColor;
        this.ctx.font = '10pt monospace';
        this.ctx.textAlign = 'right';
        this.ctx.textBaseline = 'top';
        this.ctx.fillText(`ScaleX: 1:${this.canvasData.globalScaleX}`, this.width - 10, 5);
        this.ctx.fillText(`ScaleY: 1:${this.canvasData.globalScaleY}`, this.width - 10, 16);
        this.ctx.stroke();
    }

    drawMouseTrack(x, y) {
        x = x - this.canvasData.canvasContainer.getBoundingClientRect().x;
        y = y - this.canvasData.canvasContainer.getBoundingClientRect().y;
        this.resize();
        this.drawLine(this.maxLineWidth / 2, this.axisColor, 0, y, this.width, y);
        this.drawLine(this.maxLineWidth / 2, this.axisColor, x, 0, x, this.height);
        
        let scaleX = this.canvasData.gridPixelSizeX / this.canvasData.globalScaleX;
        let scaleY = this.canvasData.gridPixelSizeY / this.canvasData.globalScaleY;

        let x_cord = (x - this.canvasData.centerX) / scaleX;
        let y_cord = -(y - this.canvasData.centerY) / scaleY;

        this.ctx.fillStyle = this.axisColor;
        this.ctx.font = '10pt monospace';
        this.ctx.textAlign = 'left';
        this.ctx.textBaseline = 'bottom';
        this.ctx.fillText(`x: ${x_cord.toFixed(2)}`, x + 5, y - 16);
        this.ctx.fillText(`y: ${y_cord.toFixed(2)}`, x + 5, y);
        this.ctx.stroke();
    }

    resize() {
        super.resize();
        this.drawSystem();
    }
}
