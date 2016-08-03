import  unittest
import transaction

from xsgs.theme.testing import INTEGRATION_TESTING
from xsgs.theme.testing import FUNCTION_TESTING

from plone.testing.z2 import Browser
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD

from zope.component import getUtility
from Products.CMFCore.utils import getToolByName

from plone.registry.interfaces import IRegistry
from plone.app.theming.interfaces import IThemeSettings

class TestSetup(unittest.TestCase):
    
    layer = FUNCTION_TESTING
    
#    def test_css_registry_configured(self):
#        portal = self.layer['portal']
#        cssRegistry = getToolByName(portal, 'portal_css')
#        self.assertTrue("++theme++xsgs.theme/css/grid.css" 
#                in cssRegistry.getResourceIds()
#            )
#        self.assertTrue("++theme++xsgs.theme/css/theme.css"
#                in cssRegistry.getResourceIds()
#            )
    
   
    def test_homepage(self):
        app = self.layer['app']
        portal = self.layer['portal']
        
        transaction.commit()
        
        browser = Browser(app)
        browser.addHeader('Authorization', 'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD,))
        
        browser.open(portal.absolute_url() + '/@@homepage')

        self.assertTrue('<div id="homepage" class="container">' in browser.contents)        
