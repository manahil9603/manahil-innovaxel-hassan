const API_BASE_URL = 'http://127.0.0.1:5000'; 


async function shortenUrl() {
    const originalUrl = document.getElementById('originalUrl').value;
    if (!originalUrl) {
        alert('Please enter a URL');
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/shorten`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: originalUrl }),
        });

        const data = await response.json();
        if (response.status === 201) {
            document.getElementById('shortUrlResult').innerText = `Short URL: ${API_BASE_URL}/${data.short_code}`;
        } else {
            document.getElementById('shortUrlResult').innerText = 'Error: ' + (data.message || 'Unknown error');
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('shortUrlResult').innerText = 'An error occurred: ' + error.message;
    }
}


async function retrieveOriginalUrl() {
    const shortCode = document.getElementById('shortCode').value;
    if (!shortCode) {
        alert('Please enter a short code');
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/shorten/${shortCode}`);
        const data = await response.json();
        if (response.status === 200) {
            document.getElementById('originalUrlResult').innerText = `Original URL: ${data.url}`;
        } else {
            document.getElementById('originalUrlResult').innerText = 'Error: ' + (data.message || 'Unknown error');
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('originalUrlResult').innerText = 'An error occurred: ' + error.message;
    }
}


async function getUrlStats() {
    const shortCode = document.getElementById('statsShortCode').value;
    if (!shortCode) {
        alert('Please enter a short code');
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/shorten/${shortCode}/stats`);
        const data = await response.json();
        if (response.status === 200) {
            document.getElementById('urlStatsResult').innerText = JSON.stringify(data, null, 2);
        } else {
            document.getElementById('urlStatsResult').innerText = 'Error: ' + (data.message || 'Unknown error');
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('urlStatsResult').innerText = 'An error occurred: ' + error.message;
    }
}