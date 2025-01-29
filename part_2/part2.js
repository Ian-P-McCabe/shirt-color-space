
async function getData(url) {
    try {
        const response = await fetch(url)
        const json = await response.json()
        return json
    } catch (error) {
        console.error(error.message)
    }
}

function createShirtColorList(colors, element) {
    colors.forEach(color => {
        // Create a container for the rectangle and text
        const itemContainer = document.createElement('div');
        itemContainer.style.textAlign = 'center';
        itemContainer.style.margin = '5px';

        // Create the rectangle
        const rect = document.createElement('div');
        rect.className = 'rectangle';
        rect.style.backgroundColor = '#' + color.Hex;

        // Create the text label
        const label = document.createElement('div');
        label.textContent = `${color["Color Name"]}`;
        label.style.marginTop = '2px';
        label.style.fontSize = '12px';
        label.style.color = '#333'; // Adjust the color as needed
        label.style.maxWidth = '75px'

        // Append the rectangle and label to the container
        itemContainer.appendChild(rect);
        itemContainer.appendChild(label);

        // Append the container to the main container
        element.appendChild(itemContainer);
    })
}
const lowestColors = await getData("https://raw.githubusercontent.com/Ian-P-McCabe/shirt-color-space/refs/heads/main/part_2/assets/lowest_random_sample_colors.json")
const lowestColorsContainer = document.getElementById("lowestRandomColors")
createShirtColorList(lowestColors, lowestColorsContainer)