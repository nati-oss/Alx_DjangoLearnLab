class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ must match this path
    context_object_name = 'library'  # ✅ variable named 'library'