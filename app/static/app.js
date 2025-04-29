document.addEventListener('DOMContentLoaded', function() {
    // Charger les actualités
    fetch('/api/news')
        .then(response => response.json())
        .then(news => {
            const container = document.getElementById('news-container');
            news.forEach(item => {
                const div = document.createElement('div');
                div.className = 'news-item';
                div.innerHTML = `<h3>${item.title}</h3><p>${item.content}</p><small>${item.date}</small>`;
                container.appendChild(div);
            });
        });
    
    // Charger les événements
    fetch('/api/events')
        .then(response => response.json())
        .then(events => {
            const container = document.getElementById('events-container');
            events.forEach(event => {
                const div = document.createElement('div');
                div.className = 'event-item';
                div.innerHTML = `<h3>${event.title}</h3><p>${event.description}</p><small>${event.date}</small>`;
                container.appendChild(div);
            });
        });
});