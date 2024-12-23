// List of hex color codes
const colors = ['#E10600', '#F2CA00', '#FF6A39', '#00965E', '#00BFB2'];

// Get the container where rectangles will be added
const container = document.getElementById('rectangleContainer');

// Create rectangles dynamically
colors.forEach(color => {
    const rect = document.createElement('div');
    rect.className = 'rectangle';
    rect.style.backgroundColor = color;
    container.appendChild(rect);
});