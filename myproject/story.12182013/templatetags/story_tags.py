from django import template
register = template.Library()

@register.simple_tag
def get_image(myStr):
	image = myStr.split(',')
	return image[0]
