.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

====================
Membership extension
====================

This module was written to extend the functionality of membership module to keep track of members membership products.

Features
--------
* Adds payment term to the membership invoice wizard

Installation
============

Install the module form Settings->Local Modules

Configuration
=============
\-

Usage
=====
Access Association menu. In members tree view there is one additional field called "Memberships" where every membership of the current member and the membership products state is presented. In addition to that in membership product's form there are two additional smart buttons created, where you can see the amount of paid and invoiced members. By clicking these buttons, user is redirected to a list of members, who have paid or invoiced that membership product.

Default view is changed from kanban to tree view in members. Geo Localization -page is hidden since it was found unneeded. Fields conserning this page are hidden from customers tree view.   


Known issues / Roadmap
======================
There's a bug in membership products smart buttons: if a membership product has 0 paid members and 1 invoiced members and the member who is invoiced has other paid membership products, then the 0 paid members button leads to this member even though it shouldn't. This is because domain applys the 2 restrictions using OR and not AND.

Credits
=======

Contributors
------------

* Aleksi Savijoki <aleksi.savijoki@tawasta.fi>
* Jarmo Kortetjärvi <jarmo.kortetjarvi@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
