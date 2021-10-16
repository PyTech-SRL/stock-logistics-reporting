import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo9-addons-oca-stock-logistics-reporting",
    description="Meta package for oca-stock-logistics-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo9-addon-stock_valued_picking_report',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 9.0',
    ]
)
