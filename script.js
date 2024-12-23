// List of hex color codes

import chosenColors from "./data/chosen-colors.json" with {type: "json"};

// const colors = ['#E10600', '#F2CA00', '#FF6A39', '#00965E', '#00BFB2'];
// Get the container where rectangles will be added
const container = document.getElementById('rectangleContainer');

// Create rectangles dynamically
chosenColors.forEach(color => {
    // Create a container for the rectangle and text
    const itemContainer = document.createElement('div');
    itemContainer.style.textAlign = 'center';
    itemContainer.style.margin = '10px';

    // Create the rectangle
    const rect = document.createElement('div');
    rect.className = 'rectangle';
    rect.style.backgroundColor = '#' + color.HEX;

    // Create the text label
    const label = document.createElement('div');
    label.textContent = `${color["Shirt Color"]}`;
    label.style.marginTop = '5px';
    label.style.fontSize = '14px';
    label.style.color = '#333'; // Adjust the color as needed

    // Append the rectangle and label to the container
    itemContainer.appendChild(rect);
    itemContainer.appendChild(label);

    // Append the container to the main container
    container.appendChild(itemContainer);
});