document.getElementById('searchInput').addEventListener('input', function() {
    const query = this.value;

    if (query.length > 0) {
        fetch(`/search?query=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                const resultsList = document.getElementById('resultsList');
                resultsList.innerHTML = '';

                data.forEach(item => {
                    const li = document.createElement('li');
                    li.textContent = item;
                    resultsList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    } else {
        document.getElementById('resultsList').innerHTML = '';
    }
});