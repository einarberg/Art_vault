document.addEventListener('DOMContentLoaded', function () {
    function registerSearchButtonHandler(){
        const searchValueElement = document.getElementById('search-value');
        searchValueElement.addEventListener('keyup',async function () {
            const searchValueElement = document.getElementById('search-value');
            const value = searchValueElement.value;
            const artworkPlaceholder = document.getElementById('artwork-search');
            const response = await fetch(`?search_filter=${value}`);

            if(response.ok) {
                const json = await response.json();
                const artworks = json.data.map(artwork =>`
                <div class="artwork-info">
                    <a href="${ artwork.id }">
                        <div>
                            <div class="artwork-thumbnail" style='background-image: url("${artwork.thumbnail}")'></div>
                        </div>
                        <h3>${artwork.title}</h3>
                        <p>${artwork.artist}</p>
                    </a>
                </div>
                
                
                `);

                artworkPlaceholder.innerHTML = artworks.join('');
            }
        });
    }

    registerSearchButtonHandler();
});