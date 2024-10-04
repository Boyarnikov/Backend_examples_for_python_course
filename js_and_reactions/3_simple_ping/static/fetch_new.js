function fetchParagraph() {
    fetch('/generate')
        .then(response => response.json())
        .then(data => {
            const newParagraph = document.createElement('p');
            newParagraph.textContent = data.paragraph;
            document.getElementById('content').appendChild(newParagraph);
        })
        .catch(error => console.error('Error fetching paragraph:', error));
}

setInterval(fetchParagraph, 1000);