
/******************************************************************************
                    GRID SIZE EVENT HANDLER
*******************************************************************************/
const submitButton = document.getElementById("sizePicker");

// create listen event for submit button pressed
submitButton.addEventListener("submit",
    function(event) {
        event.preventDefault();
        let heightVal = event.target[0].value;     // store height val
        let widthVal = event.target[1].value;      // store width val
        makeGrid(heightVal, widthVal);             // make grid with return vals
    }
);

function makeGrid(height, width) {

    // remove any squares already present
    while (document.querySelector("tr") != null) {
        canvas.firstChild.remove();
    }

    // build the grid
    for (let row = 0; row < height; row++) {
        let canvasRow = document.createElement("tr");   // create tr element
        canvas.appendChild(canvasRow);                  // append to canvas
        for (let col = 0; col < width; col++) {
            let square = document.createElement("td");  // create td element
            canvasRow.appendChild(square);              // append to row
        }
    }
}

/******************************************************************************
                    COLOR PICK EVENT AND HANDLER
*******************************************************************************/
const colorPicker = document.getElementById("colorPicker");
var colorVal;

colorPicker.addEventListener("change",
    function(event) {
        colorVal = event.target.value;
    }
);

/******************************************************************************
                    CANVAS CLICK EVENT HANDLER
*******************************************************************************/
const canvas = document.getElementById("pixelCanvas");  // parent elem of grid

// add a listen for clicking on the canvas
canvas.addEventListener("click",
    function(event){
        canvasClicked(event, event.target, colorVal)
    }
);

// handle canvas click events: change color
function canvasClicked(event, square, color) {
    if (event.target.nodeName === "TD") {     // only work on td elements
        if (color === undefined) {            // set color to black if undefined
            color = "#000000"
        };
        square.style.backgroundColor = color;
    }
}
