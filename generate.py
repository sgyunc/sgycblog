import os
import yaml
import markdown
from datetime import datetime

def generate_html(set_yaml, output_folder, posts_folder):
    # 读取 set.yml 文件
    with open(set_yaml, 'r', encoding='utf-8') as set_file:
        set_data = yaml.load(set_file, Loader=yaml.FullLoader)

    # 获取当前年份
    current_year = datetime.now().year

    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 生成每篇文章的详情页
    for filename in os.listdir(posts_folder):
        if filename.endswith('.md'):
            md_filepath = os.path.join(posts_folder, filename)
            with open(md_filepath, 'r', encoding='utf-8') as md_file:
                md_content = md_file.read()
                html_content = markdown.markdown(md_content)

                # 从 Markdown 文件中提取标题和时间
                title = None
                date = None
                for line in md_content.split('\n'):
                    if line.startswith('title:'):
                        title = line.split(':', 1)[1].strip()
                    elif line.startswith('date:'):
                        date = line.split(':', 1)[1].strip()

                if title:
                    # 生成详情页 HTML 文件
                    output_filepath = os.path.join(output_folder, f'{title.lower().replace(" ", "_")}.html')
                    with open(output_filepath, 'w', encoding='utf-8') as output:
                        output.write('<!DOCTYPE html>\n')
                        output.write('<html lang="en">\n')
                        output.write('<head>\n')
                        output.write('    <meta charset="UTF-8">\n')

                        # 写入额外的 meta 标签
                        if 'meta_tags' in set_data:
                            for meta_tag in set_data['meta_tags']:
                                output.write(f'    {meta_tag}\n')

                        # 引入 CSS 文件
                        if 'css' in set_data:
                            for css_file in set_data['css']:
                                output.write(f'    <link rel="stylesheet" type="text/css" href="{css_file}">\n')

                        output.write(f'    <title>{os.path.splitext(os.path.basename(md_filepath))[0]}</title>\n')
                        output.write('</head>\n')
                        output.write('<body>\n')

                        output.write('    <nav>\n')
                        output.write(f'        <h1>{set_data["header_title"]}</h1>\n')
                        output.write('        <ul>\n')
                        for nav_item in set_data.get('nav', []):
                            output.write(f'            <li><a href="{nav_item["link"]}">{nav_item["name"]}</a></li>\n')
                        output.write('</ul>\n')

                        output.write('    </nav>\n')

                        output.write(f'    <div class="content">\n')
                        output.write(f'        <h1>{title}</h1>\n')
                        output.write(f'        <p class="date">Published on: {date}</p>\n')
                        output.write(html_content)
                        output.write('    </div>\n')

                        # 引入 JS 文件
                        if 'js' in set_data:
                            for js_file in set_data['js']:
                                output.write(f'    <script src="{js_file}"></script>\n')

                        # 添加页脚
                        output.write('<footer>\n')
                        output.write(f'        <p>{set_data["footer_text"]} &copy;{current_year} by {set_data["footer_by"]}</p>\n')
                        output.write('</footer>\n')

                        output.write('</body>\n')
                        output.write('</html>\n')

    # 生成首页 HTML 文件
    with open(os.path.join(output_folder, 'index.html'), 'w', encoding='utf-8') as output:
        output.write('<!DOCTYPE html>\n')
        output.write('<html lang="en">\n')
        output.write('<head>\n')
        output.write('    <meta charset="UTF-8">\n')

        # 写入额外的 meta 标签
        if 'meta_tags' in set_data:
            for meta_tag in set_data['meta_tags']:
                output.write(f'    {meta_tag}\n')

        # 引入 CSS 文件
        if 'css' in set_data:
            for css_file in set_data['css']:
                output.write(f'    <link rel="stylesheet" type="text/css" href="{css_file}">\n')

        output.write(f'    <title>{set_data["title"]}</title>\n')
        output.write(f'    <meta name="keywords" content="{set_data["keywords"]}">\n')
        output.write('</head>\n')
        output.write('<body>\n')

        output.write('    <nav>\n')
        output.write(f'        <h1>{set_data["header_title"]}</h1>\n')
        output.write('        <ul>\n')
        for nav_item in set_data.get('nav', []):
            output.write(f'            <li><a href="{nav_item["link"]}">{nav_item["name"]}</a></li>\n')
        output.write('</ul>\n')
        output.write('<input type="text" id="searchInput" placeholder="搜索文章">\n')


        output.write('    </nav>\n')
        output.write('<div id="searchResults"></div>\n')

        output.write('    <div class="content">\n')

        # 生成文章列表链接
        for filename in os.listdir(posts_folder):
            if filename.endswith('.md'):
                md_filepath = os.path.join(posts_folder, filename)
                with open(md_filepath, 'r', encoding='utf-8') as md_file:
                    md_content = md_file.read()

                    # 从 Markdown 文件中提取标题和时间
                    title = None
                    date = None
                    for line in md_content.split('\n'):
                        if line.startswith('title:'):
                            title = line.split(':', 1)[1].strip()
                        elif line.startswith('date:'):
                            date = line.split(':', 1)[1].strip()

                    if title:
                        # 生成文章链接
                        output.write(f'        <h2><a href="{title.lower().replace(" ", "_")}.html">{title}</a></h2>\n')

                        # 插入时间到首页
                        if date:
                            output.write(f'        <p class="date">Published on: {date}</p>\n')

                        # 从 Markdown 文件中提取摘要
                        abstract = None
                        for line in md_content.split('\n'):
                            if line.startswith('## '):
                                abstract = line[3:].strip()
                                break

                        # 插入摘要到首页
                        if abstract:
                            output.write(f'        <p>{abstract}</p>\n')

        output.write('    </div>\n')

        # 引入 JS 文件
        if 'js' in set_data:
            for js_file in set_data['js']:
                output.write(f'    <script src="{js_file}"></script>\n')

        # 添加页脚
        output.write('<footer>\n')
        output.write(f'        <p>{set_data["footer_text"]} &copy;{current_year} by {set_data["footer_by"]}</p>\n')
        output.write('</footer>\n')

        output.write('</body>\n')
        output.write('</html>\n')

    # 生成归档页面 HTML 文件
    with open(os.path.join(output_folder, 'archive.html'), 'w', encoding='utf-8') as output:
        output.write('<!DOCTYPE html>\n')
        output.write('<html lang="en">\n')
        output.write('<head>\n')
        output.write('    <meta charset="UTF-8">\n')

        # 写入额外的 meta 标签
        if 'meta_tags' in set_data:
            for meta_tag in set_data['meta_tags']:
                output.write(f'    {meta_tag}\n')

        # 引入 CSS 文件
        if 'css' in set_data:
            for css_file in set_data['css']:
                output.write(f'    <link rel="stylesheet" type="text/css" href="{css_file}">\n')

        output.write(f'    <title>{set_data["title"]} - Archive</title>\n')
        output.write(f'    <meta name="keywords" content="{set_data["keywords"]}">\n')
        output.write('</head>\n')
        output.write('<body>\n')

        output.write('    <nav>\n')
        output.write(f'        <h1>{set_data["header_title"]} - Archive</h1>\n')
        output.write('        <ul>\n')
        for nav_item in set_data.get('nav', []):
            output.write(f'            <li><a href="{nav_item["link"]}">{nav_item["name"]}</a></li>\n')
        output.write('</ul>\n')
        output.write('    </nav>\n')

        output.write('    <div class="content">\n')

        # 生成文章列表链接
        for filename in os.listdir(posts_folder):
            if filename.endswith('.md'):
                md_filepath = os.path.join(posts_folder, filename)
                with open(md_filepath, 'r', encoding='utf-8') as md_file:
                    md_content = md_file.read()

                    # 从 Markdown 文件中提取标题和时间
                    title = None
                    date = None
                    for line in md_content.split('\n'):
                        if line.startswith('title:'):
                            title = line.split(':', 1)[1].strip()
                        elif line.startswith('date:'):
                            date = line.split(':', 1)[1].strip()

                    if title:
                        # 生成文章链接
                        output.write(f'        <h2><a href="{title.lower().replace(" ", "_")}.html">{title}</a> - {date}</h2>\n')

                        # 从 Markdown 文件中提取摘要
                        abstract = None
                        for line in md_content.split('\n'):
                            if line.startswith('## '):
                                abstract = line[3:].strip()
                                break

                        # 插入摘要到归档页面
                        if abstract:
                            output.write(f'        <p>{abstract}</p>\n')

        output.write('    </div>\n')

        # 引入 JS 文件
        if 'js' in set_data:
            for js_file in set_data['js']:
                output.write(f'    <script src="{js_file}"></script>\n')

        # 添加页脚
        output.write('<footer>\n')
        output.write(f'        <p>{set_data["footer_text"]} &copy;{current_year} by {set_data["footer_by"]}</p>\n')
        output.write('</footer>\n')

        output.write('</body>\n')
        output.write('</html>\n')

# 在 generate_html 函数中添加以下代码段

    # 生成分类页面 HTML 文件
    categories = {}  # 存储文章分类信息
    for filename in os.listdir(posts_folder):
        if filename.endswith('.md'):
            md_filepath = os.path.join(posts_folder, filename)
            with open(md_filepath, 'r', encoding='utf-8') as md_file:
                md_content = md_file.read()

                # 从 Markdown 文件中提取分类、标题和时间
                category = None
                title = None
                date = None
                for line in md_content.split('\n'):
                    if line.startswith('category:'):
                        category = line.split(':', 1)[1].strip()
                    elif line.startswith('title:'):
                        title = line.split(':', 1)[1].strip()
                    elif line.startswith('date:'):
                        date = line.split(':', 1)[1].strip()

                if category and title:
                    # 添加文章到分类信息中
                    if category not in categories:
                        categories[category] = []
                    categories[category].append({'title': title, 'date': date})

    # 生成总的分类页面
    output_filepath_all = os.path.join(output_folder, 'categories.html')
    with open(output_filepath_all, 'w', encoding='utf-8') as output_all:
        output_all.write('<!DOCTYPE html>\n')
        output_all.write('<html lang="en">\n')
        output_all.write('<head>\n')
        output_all.write('    <meta charset="UTF-8">\n')

        # 写入额外的 meta 标签
        if 'meta_tags' in set_data:
            for meta_tag in set_data['meta_tags']:
                output_all.write(f'    {meta_tag}\n')

        # 引入 CSS 文件
        if 'css' in set_data:
            for css_file in set_data['css']:
                output_all.write(f'    <link rel="stylesheet" type="text/css" href="{css_file}">\n')

        output_all.write(f'    <title>{set_data["title"]} - All Categories</title>\n')
        output_all.write(f'    <meta name="keywords" content="{set_data["keywords"]}">\n')
        output_all.write('</head>\n')
        output_all.write('<body>\n')

        output_all.write('    <nav>\n')
        output_all.write(f'        <h1>{set_data["header_title"]} - All Categories</h1>\n')
        output_all.write('        <ul>\n')  # 这里修正过来
        for nav_item in set_data.get('nav', []):
            output_all.write(f'            <li><a href="{nav_item["link"]}">{nav_item["name"]}</a></li>\n')
        output_all.write('        </ul>\n')  # 这里也修正过来
        output_all.write('    </nav>\n')

        output_all.write('    <div class="content">\n')

        # 生成分类链接
        for category in categories:
            output_all.write(f'        <h2><a href="{category.lower().replace(" ", "_")}_category.html">{category}</a></h2>\n')

        output_all.write('    </div>\n')

        # 引入 JS 文件
        if 'js' in set_data:
            for js_file in set_data['js']:
                output_all.write(f'    <script src="{js_file}"></script>\n')

        # 添加页脚
        output_all.write('<footer>\n')
        output_all.write(f'        <p>{set_data["footer_text"]} &copy;{current_year} by {set_data["footer_by"]}</p>\n')
        output_all.write('</footer>\n')

        output_all.write('</body>\n')
        output_all.write('</html>\n')

    # 生成分类页面
    for category, articles in categories.items():
        output_filepath = os.path.join(output_folder, f'{category.lower().replace(" ", "_")}_category.html')
        with open(output_filepath, 'w', encoding='utf-8') as output:
            output.write('<!DOCTYPE html>\n')
            output.write('<html lang="en">\n')
            output.write('<head>\n')
            output.write('    <meta charset="UTF-8">\n')

            # 写入额外的 meta 标签
            if 'meta_tags' in set_data:
                for meta_tag in set_data['meta_tags']:
                    output.write(f'    {meta_tag}\n')

            # 引入 CSS 文件
            if 'css' in set_data:
                for css_file in set_data['css']:
                    output.write(f'    <link rel="stylesheet" type="text/css" href="{css_file}">\n')

            output.write(f'    <title>{set_data["title"]} - {category} Category</title>\n')
            output.write(f'    <meta name="keywords" content="{set_data["keywords"]}">\n')
            output.write('</head>\n')
            output.write('<body>\n')

            output.write('    <nav>\n')
            output.write(f'        <h1>{set_data["header_title"]} - {category} Category</h1>\n')
            output.write('        <ul>\n')
            for nav_item in set_data.get('nav', []):
                output.write(f'            <li><a href="{nav_item["link"]}">{nav_item["name"]}</a></li>\n')
            output.write('</ul>\n')
            output.write('    </nav>\n')

            output.write('    <div class="content">\n')

            # 生成文章列表链接
            for article in articles:
                title = article['title']
                date = article['date']
                output.write(f'        <h2><a href="{title.lower().replace(" ", "_")}.html">{title}</a> - {date}</h2>\n')

            output.write('    </div>\n')

            # 引入 JS 文件
            if 'js' in set_data:
                for js_file in set_data['js']:
                    output.write(f'    <script src="{js_file}"></script>\n')

            # 添加页脚
            output.write('<footer>\n')
            output.write(f'        <p>{set_data["footer_text"]} &copy;{current_year} by {set_data["footer_by"]}</p>\n')
            output.write('</footer>\n')

            output.write('</body>\n')
            output.write('</html>\n')


    # 生成友链页面 HTML 文件
    output_filepath_links = os.path.join(output_folder, 'links.html')
    with open(output_filepath_links, 'w', encoding='utf-8') as output_links:
        output_links.write('<!DOCTYPE html>\n')
        output_links.write('<html lang="en">\n')
        output_links.write('<head>\n')
        output_links.write('    <meta charset="UTF-8">\n')

        # 写入额外的 meta 标签
        if 'meta_tags' in set_data:
            for meta_tag in set_data['meta_tags']:
                output_links.write(f'    {meta_tag}\n')

        # 引入 CSS 文件
        if 'css' in set_data:
            for css_file in set_data['css']:
                output_links.write(f'    <link rel="stylesheet" type="text/css" href="{css_file}">\n')

        output_links.write(f'    <title>{set_data["title"]} - Links</title>\n')
        output_links.write(f'    <meta name="keywords" content="{set_data["keywords"]}">\n')
        output_links.write('</head>\n')
        output_links.write('<body>\n')

        output_links.write('    <nav>\n')
        output_links.write(f'        <h1>{set_data["header_title"]} - Links</h1>\n')
        output_links.write('        <ul>\n')
        for nav_item in set_data.get('nav', []):
            output_links.write(f'            <li><a href="{nav_item["link"]}">{nav_item["name"]}</a></li>\n')
        output_links.write('</ul>\n')
        output_links.write('    </nav>\n')

        output_links.write('    <div class="content">\n')

        # 生成友链
        for link_data in set_data.get('links', []):
            name = link_data.get('name', '')
            link = link_data.get('link', '')
            avatar = link_data.get('avatar', '')
            descr = link_data.get('descr', '')

            if name and link:
                output_links.write('        <div class="link-item">\n')
                output_links.write(f'            <div class="avatar"><img src="{avatar}" alt="{name}"></div>\n')
                output_links.write(f'            <div class="info">\n')
                output_links.write(f'                <h2><a href="{link}" target="_blank">{name}</a></h2>\n')
                if descr:
                    output_links.write(f'                <p>{descr}</p>\n')
                output_links.write('            </div>\n')
                output_links.write('        </div>\n')

        output_links.write('    </div>\n')

        # 引入 JS 文件
        if 'js' in set_data:
            for js_file in set_data['js']:
                output_links.write(f'    <script src="{js_file}"></script>\n')

        # 添加页脚
        output_links.write('<footer>\n')
        output_links.write(f'        <p>{set_data["footer_text"]} &copy;{current_year} by {set_data["footer_by"]}</p>\n')
        output_links.write('</footer>\n')

        output_links.write('</body>\n')
        output_links.write('</html>\n')


if __name__ == "__main__":
    generate_html('set.yml', './public', './posts_folder')
