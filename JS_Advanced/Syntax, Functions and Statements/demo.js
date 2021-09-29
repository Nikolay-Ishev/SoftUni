
 
function distance(x1, y1, x2, y2) {
        let distH = x1 - x2;
        let distY = y1 - y2;
        console.log(Math.sqrt(distH**2 + distY**2))
        return Math.sqrt(distH**2 + distY**2);
    }

distance(2, 1, 0, 0)
