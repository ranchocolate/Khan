// Main JavaScript for Khan application

console.log('Khan app loaded');

// Helper function to fetch API data
async function fetchData(endpoint) {
    try {
        const response = await fetch(endpoint);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Error fetching data:', error);
        return null;
    }
}

// Load topics on home page
document.addEventListener('DOMContentLoaded', () => {
    // Any page initialization code here
});
