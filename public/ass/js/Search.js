document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');

    searchInput.addEventListener('input', function () {
        const searchTerm = searchInput.value.toLowerCase();

        // 清空之前的搜索结果
        searchResults.innerHTML = '';

        // 如果搜索关键字为空，直接返回，不执行搜索逻辑
        if (!searchTerm.trim()) {
            return;
        }

        // 遍历文章标题，查找包含搜索关键字的文章
        const articles = document.querySelectorAll('.content h2');
        articles.forEach(function (article) {
            const title = article.innerText.toLowerCase();
            if (title.includes(searchTerm)) {
                // 创建搜索结果项，并添加点击事件，点击后直接进入文章详情页
                const resultItem = document.createElement('div');
                resultItem.innerHTML = `<a href="${title.toLowerCase().replace(' ', '_')}.html">${title}</a>`;
                searchResults.appendChild(resultItem);
            }
        });
    });
});
