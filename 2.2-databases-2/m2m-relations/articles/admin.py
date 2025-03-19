from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
	def clean(self):
		super().clean()

		main_count = sum(1 for form in self.forms if form.cleaned_data.get('is_main'))

		if main_count == 0:
			raise ValidationError("Должен быть хотя бы один основной тег.")

		if main_count > 1:
			raise ValidationError("Может быть только один основной тег.")

		return super().clean()


class ScopeInline(admin.TabularInline):
	model = Scope
	formset = ScopeInlineFormset
	extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	inlines = [ScopeInline]
	list_display = ('title', 'published_at')
	search_fields = ('title',)
	ordering = ('-published_at',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)
