import re
from pages.views import render
from pages.models import Page


class LocalMiddleWare(object):

    def __init__(self):
        self.content_name=''
        self.content_id=''
        self.status=0;


    def process_request(self, request):
        #test_string="this is only gor teting purpose";#request.get_full_path();
        current_path = request.path
        if (not current_path.startswith('/static') and not current_path.startswith('/admin') and not current_path.startswith('/api') and
            not current_path.startswith('/login') and not current_path.startswith('/logout')):

            page, _ = Page.get_current_page(current_path)

            setattr(request, 'page', page)


        #now check for the regular expressio

        # check for the id

        # call for the render function
        #return render( request, 'index.html' , {'name':request.new_var})

