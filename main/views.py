from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Iwakura Succession',
        'amount': '8',
        'description': 'After casting an Element Skill, gain 1 Succession Seed. This effect can be triggered once every 5s. The Succession Seeds may exist simultaneously. After using an Elemental Burst, all Succession Seeds are consumed and after 2s, the character regenerates 7.5 Energy of each seed consumed.'
    }

    return render(request, "main.html", context)