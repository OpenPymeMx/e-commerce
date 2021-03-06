import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-e-commerce",
    description="Meta package for oca-e-commerce Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-website_sale_checkout_country_vat',
        'odoo12-addon-website_sale_product_attribute_filter_visibility',
        'odoo12-addon-website_sale_require_legal',
        'odoo12-addon-website_sale_require_login',
        'odoo12-addon-website_sale_show_company_data',
        'odoo12-addon-website_sale_suggest_create_account',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
