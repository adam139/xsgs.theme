import unittest
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
    
    layer = INTEGRATION_TESTING
    

    
    def test_theme_configured(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IThemeSettings)
        self.assertEqual(settings.enabled, True)
        import pdb
        pdb.set_trace()
        self.assertEqual(settings.rules, 
                "/++theme++xsgs.theme/rules.xml"
            )
        self.assertEqual(settings.absolutePrefix,
                "/++theme++xsgs.theme"
            )

class TestRendering(unittest.TestCase):
    
    layer = FUNCTION_TESTING
    
    def test_render_plone_page(self):
        app = self.layer['app']
        portal = self.layer['portal']
        
        transaction.commit()
        
        browser = Browser(app)
        #open('/tmp/test.html','w').write(browser.contents)    
        browser.open(portal.absolute_url())
        self.assertTrue('<div id="site-scripts">' in browser.contents)
    
                
    def test_render_zmi_page(self):
        app = self.layer['app']
        portal = self.layer['portal']
        
        transaction.commit()
        
        browser = Browser(app)
        browser.addHeader('Authorization', 'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD,))
        
        browser.open(portal.absolute_url() + '/manage_main')
        
        self.assertFalse('<body class="plonesite">' in browser.contents)
