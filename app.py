let jsonData = [];

// Fetch and load JSON data
fetch('jsondata.json')
    .then(response => response.json())
    .then(data => {
        jsonData = data;
        populateFilterOptions();
        displayData(jsonData);
    })
    .catch(error => console.error('Error loading JSON data:', error));

// Populate filter dropdowns with unique values
function populateFilterOptions() {
    const filters = ['end_year', 'topic', 'sector', 'region'];
    filters.forEach(filter => {
        const filterElement = document.getElementById(filter);
        const uniqueValues = [...new Set(jsonData.map(item => item[filter]).filter(val => val))];
        uniqueValues.forEach(value => {
            const option = document.createElement('option');
            option.value = value;
            option.textContent = value;
            filterElement.appendChild(option);
        });
    });
}

// Filter the data based on selected filters
function filterData() {
    const filters = {
        end_year: document.getElementById('end_year').value,
        topic: document.getElementById('topic').value,
        sector: document.getElementById('sector').value,
        region: document.getElementById('region').value,
    };

    const filteredData = jsonData.filter(item => {
        return (!filters.end_year || item.end_year === filters.end_year) &&
               (!filters.topic || item.topic === filters.topic) &&
               (!filters.sector || item.sector === filters.sector) &&
               (!filters.region || item.region === filters.region);
    });

    displayData(filteredData);
}

// Display the filtered or full data
function displayData(data) {
    const dataDisplay = document.getElementById('data-display');
    dataDisplay.innerHTML = '';

    data.forEach(item => {
        const dataItem = document.createElement('div');
        dataItem.className = 'data-item';
        dataItem.innerHTML = `
            <p><strong>Title:</strong> ${item.title}</p>
            <p><strong>Insight:</strong> ${item.insight}</p>
            <p><strong>End Year:</strong> ${item.end_year}</p>
            <p><strong>Topic:</strong> ${item.topic}</p>
            <p><strong>Sector:</strong> ${item.sector}</p>
            <p><strong>Region:</strong> ${item.region}</p>
            <p><strong>Country:</strong> ${item.country}</p>
        `;
        dataDisplay.appendChild(dataItem);
    });
}
