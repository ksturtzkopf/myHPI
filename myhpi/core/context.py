from wagtail.core.models import Page, Site

from .models import BasePage
from .utils import get_user_groups


def base_context(request):
    # How wagtail page trees work: https://www.accordbox.com/blog/how-to-create-and-manage-menus-in-wagtail/

    # Fetch all pages
    root_page = getattr(Site.find_for_request(request), "root_page", None)
    pages = BasePage.objects.in_menu().live()
    pages_visible_for_user = []
    path_map = {}
    depth_levels = set()

    if not root_page:
        return {"root_page": None, "all_pages": None, "nav_root_pages": None}

    # Add root page to path map - only needed if root page is NOT a base page (yet)
    root_page.menu_children = []
    path_map[root_page.path] = root_page

    # Determine all pages the user may view based on his groups
    user_groups = get_user_groups(request.user)

    pages_visible_for_user = pages.filter(visible_for__in=user_groups)

    # Add additional properties to each page and save in path_map
    # The path of each page is represented by a string, each level labeled with 4 chars
    for page in pages:
        page.menu_children = []
        page.is_leaf = True
        path_map[page.path] = page
        depth_levels.add(page.depth)

    # Iterate over all depth levels of the tree, going from leaves to root
    # Mark any parent nodes as non-leaves
    # If page is allowed to be viewed and (it has viewable children or is a leaf),
    # add it to the parent's viewable children
    while depth_levels:
        deepest_level = max(depth_levels)
        for path, page in path_map.items():
            page = path_map[path]
            if page.depth != deepest_level:
                continue
            parent_path = page.path[:-4]
            if parent_path in path_map:
                path_map[parent_path].is_leaf = False
                page_allowed_to_be_viewed = page in pages_visible_for_user or page.is_public
                page_has_children_or_is_leaf = page.menu_children or page.is_leaf
                if page_allowed_to_be_viewed and page_has_children_or_is_leaf:
                    path_map[parent_path].menu_children.append(page)
        depth_levels.remove(deepest_level)

    # Return root page and all of their children
    root_children = path_map[root_page.path].menu_children
    return {
        "root_page": root_page,
        "all_pages": root_children,
        "nav_root_pages": Page.objects.in_menu().child_of(root_page) if root_page else None,
    }
