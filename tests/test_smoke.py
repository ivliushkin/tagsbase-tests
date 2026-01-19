# Checking the availability of all static and dynamic pages

def test_home_page_status(client):
    response = client.get('/')
    assert response.status_code == 200

def test_about_page_status(client):
    response = client.get('/about')
    assert response.status_code == 200

def test_contact_page_status(client):
    response = client.get('/contact')
    assert response.status_code == 200

def test_advertisers_page_status(client):
    response = client.get('/advertisers')
    assert response.status_code == 200

def test_legal_page_status(client):
    response = client.get('/legal')
    assert response.status_code == 200

def test_all_brands_page_status(client):
    response = client.get('/brands')
    assert response.status_code == 200

def test_brand_detail_page(client):
    response = client.get('/brand/ASICS')
    assert response.status_code == 200
    assert b"ASICS" in response.data
    assert b"Running performance brand." in response.data

def test_sitemap_page_status(client):
    response = client.get('/sitemap.xml')
    assert response.status_code == 200

def test_nonexistent_page(client):
    """Проверяет, что несуществующая страница возвращает 404."""
    response = client.get('/nonexistent-page')
    assert response.status_code == 404
