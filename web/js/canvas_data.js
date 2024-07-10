let scale_index = [
    1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000
];

export class CanvasData {
    constructor(globalScale, pos_x, neg_x, pos_y, neg_y) {
        this.canvasContainer = document.querySelector('.graph-canvas');

        this.globalScaleX = globalScale;
        this.globalScaleY = globalScale;

        this.startPosX = pos_x;
        this.startNegX = neg_x;
        this.startPosY = pos_y;
        this.startNegY = neg_y;
    }

    init() {
        this.pos_x = this.startPosX + (this.startPosX % this.globalScaleX);
        this.neg_x = this.startNegX - (this.globalScaleX - (Math.abs(this.startNegX) % this.globalScaleX === 0 ? this.globalScaleX : Math.abs(this.startNegX) % this.globalScaleX));
        this.pos_y = this.startPosY + (this.startPosY % this.globalScaleY);
        this.neg_y = this.startNegY - (this.globalScaleY - (Math.abs(this.startNegY) % this.globalScaleY === 0 ? this.globalScaleY : Math.abs(this.startNegY) % this.globalScaleY));

        this.gridPixelSizeX = this.width / ((this.pos_x - this.neg_x) / this.globalScaleX + 2);
        this.gridPixelSizeY = this.height / ((this.pos_y - this.neg_y) / this.globalScaleY + 2);
        
        this.findGlobalScaleX();
        this.findGlobalScaleY();

        this.resize()
    }

    findGlobalScaleX() {
        if (this.gridPixelSizeX > 50) {
            return ;
        }
        this.globalScaleX = upperScale(this.globalScaleX);
        this.pos_x = this.startPosX + (this.startPosX % this.globalScaleX);
        this.neg_x = this.startNegX - (this.globalScaleX - (Math.abs(this.startNegX) % this.globalScaleX === 0 ? this.globalScaleX : Math.abs(this.startNegX) % this.globalScaleX));

        this.gridPixelSizeX = this.width / ((this.pos_x - this.neg_x) / this.globalScaleX + 2);
        this.findGlobalScaleX();
    }

    findGlobalScaleY() {
        if (this.gridPixelSizeY > 40) {
            return ;
        }
        this.globalScaleY = upperScale(this.globalScaleY);
        this.pos_y = this.startPosY + (this.startPosY % this.globalScaleY);
        this.neg_y = this.startNegY - (this.globalScaleY - (Math.abs(this.startNegY) % this.globalScaleY === 0 ? this.globalScaleY : Math.abs(this.startNegY) % this.globalScaleY));

        this.gridPixelSizeY = this.height / ((this.pos_y - this.neg_y) / this.globalScaleY + 2);
        this.findGlobalScaleY();
    }

    get width() {
        return this.canvasContainer.clientWidth;
    }

    get height() {
        return this.canvasContainer.clientHeight;
    }

    get centerX() {
        return (0 - this.neg_x + this.globalScaleX) / this.globalScaleX * this.gridPixelSizeX;
    }

    get centerY() {
        return (0 + this.pos_y + this.globalScaleY) / this.globalScaleY * this.gridPixelSizeY;
    }

    resize() {
        let prevPixelSizeX = this.gridPixelSizeX;
        let prevPixelSizeY = this.gridPixelSizeY;
        this.gridPixelSizeX = this.width / ((this.pos_x - this.neg_x) / this.globalScaleX + 2);
        this.gridPixelSizeY = this.height / ((this.pos_y - this.neg_y) / this.globalScaleY + 2);

        if (this.gridPixelSizeX - prevPixelSizeX < 0 && this.gridPixelSizeX < 50) {
            this.globalScaleX = upperScale(this.globalScaleX);
        }
        else if (this.gridPixelSizeX - prevPixelSizeX > 0 && this.gridPixelSizeX > 100) {
            this.globalScaleX = lowerScale(this.globalScaleX);
        }

        if (this.gridPixelSizeY - prevPixelSizeY < 0 && this.gridPixelSizeY < 50) {
            this.globalScaleY = upperScale(this.globalScaleY);
        }
        else if (this.gridPixelSizeY - prevPixelSizeY > 0 && this.gridPixelSizeY > 70) {
            this.globalScaleY = lowerScale(this.globalScaleY);
        }

        this.pos_x = this.startPosX + (this.startPosX % this.globalScaleX);
        this.pos_y = this.startPosY + (this.startPosY % this.globalScaleY);
        this.neg_x = this.startNegX - (this.globalScaleX - (Math.abs(this.startNegX) % this.globalScaleX === 0 ? this.globalScaleX : Math.abs(this.startNegX) % this.globalScaleX));
        this.neg_y = this.startNegY - (this.globalScaleY - (Math.abs(this.startNegY) % this.globalScaleY === 0 ? this.globalScaleY : Math.abs(this.startNegY) % this.globalScaleY));

        this.gridPixelSizeX = this.width / ((this.pos_x - this.neg_x) / this.globalScaleX + 2);
        this.gridPixelSizeY = this.height / ((this.pos_y - this.neg_y) / this.globalScaleY + 2);
    }
}

function upperScale(scale) {
    return scale_index[scale_index.indexOf(scale) + 1];
}

function lowerScale(scale) {
    if (scale === 1) {
        return 1;
    }
    return scale_index[scale_index.indexOf(scale) - 1];
}
