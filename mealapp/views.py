from django.shortcuts import redirect, render
import requests
import random

# Главная страница
def main(request):

    # Random meals 
    letters_for_rondom = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'v', 'w', 'y']
    rand0m_letters = random.choices(letters_for_rondom, k=8)
    all_img_random_meals = []
    all_random_meals = []
    id = []
    for i in rand0m_letters:
        all_total = zip(all_random_meals, all_img_random_meals, id)
        API_URL = f'https://www.themealdb.com/api/json/v1/1/search.php?f={i}'
        res = requests.get(API_URL)
        jeyson = res.json()
        run = len(jeyson['meals'])
        l = []
        r = 0 
        while r != run:
            r=r+1
            l.append(r)
        l.pop()
        l.insert(0,0)
        l_len = len(l)
        l_len2 = l_len-1
        l_random = random.randint(0, l_len2)
        random_meal = jeyson['meals'][l_random]['strMeal']
        random_meal_id = jeyson['meals'][l_random]['idMeal']
        random_img = jeyson['meals'][l_random]['strMealThumb']
        all_img_random_meals.append(random_img)
        id.append(random_meal_id)
        all_random_meals.append(random_meal)

# --------------------------------------------------------------------------------------------------
# Random ingridients 
    total_random_ingridients = []
    img_random_ingridients = []
    all_total_random_ingridients = zip(img_random_ingridients, total_random_ingridients)
    API_URL_random_ingridients = 'https://www.themealdb.com/api/json/v1/1/list.php?i=list'
    res_random_ingridients = requests.get(API_URL_random_ingridients)
    jeyson_random_ingridients = res_random_ingridients.json()
    run_random_ingridients = len(jeyson['meals'])
    i_random_ingridients = 0
    ii_random_ingridients = []
    while i_random_ingridients != run_random_ingridients:
        i_random_ingridients=i_random_ingridients+1
        ii_random_ingridients.append(i_random_ingridients)
    ii_random_ingridients.insert(0,0)
    ii_random_ingridients.pop()
    rand0m_random_ingridients = random.choices(ii_random_ingridients, k=4)
    for y_random_ingridients in rand0m_random_ingridients:
        all_meals_random_ingridients = jeyson_random_ingridients['meals'][y_random_ingridients]['strIngredient']
        total_random_ingridients.append(all_meals_random_ingridients)
    for im_random_ingridients in total_random_ingridients:
        images_random_ingridients = f'https://www.themealdb.com/images/ingredients/{im_random_ingridients}.png'
        img_random_ingridients.append(images_random_ingridients)

#---------------------------------------------------------------------------------------------------
# Latest Meals
    # chivito 
    API_URL = f'https://www.themealdb.com/api/json/v1/1/search.php?f=c'
    res = requests.get(API_URL)
    jeyson = res.json()
    chivito = jeyson['meals'][-1]['strMeal']
    chivito_img = jeyson['meals'][-1]['strMealThumb']

    # walnut 
    API_URL1 = f'https://www.themealdb.com/api/json/v1/1/search.php?f=w'
    res1 = requests.get(API_URL1)
    jeyson1 = res1.json()
    walnut = jeyson1['meals'][-1]['strMeal']
    walnut_img = jeyson1['meals'][-1]['strMealThumb']

    # fresh sardines
    API_URL2 = f'https://www.themealdb.com/api/json/v1/1/search.php?f=f'
    res2 = requests.get(API_URL2)
    jeyson2 = res2.json()
    fresh_sardines = jeyson2['meals'][-1]['strMeal']
    fresh_sardines_img = jeyson2['meals'][-1]['strMealThumb']

    # Burek 
    API_URL3 = f'https://www.themealdb.com/api/json/v1/1/search.php?f=b'
    res3 = requests.get(API_URL3)
    jeyson3 = res3.json()
    burek = jeyson3['meals'][-1]['strMeal']
    burek_img = jeyson3['meals'][-1]['strMealThumb']

    # Mashroom
    API_URL4 = f'https://www.themealdb.com/api/json/v1/1/search.php?f=m'
    res4 = requests.get(API_URL4)
    jeyson4 = res4.json()
    mashroom = jeyson4['meals'][-1]['strMeal']
    mashroom_img = jeyson4['meals'][-1]['strMealThumb']


    # Croatian Bean
    API_URL5 = f'https://www.themealdb.com/api/json/v1/1/search.php?f=c'
    res5 = requests.get(API_URL5)
    jeyson5 = res5.json()
    croatian = jeyson5['meals'][-2]['strMeal']
    croatian_img = jeyson5['meals'][-2]['strMealThumb']

    # Croatian Lamb
    API_URL6 = f'https://www.themealdb.com/api/json/v1/1/search.php?f=c'
    res6 = requests.get(API_URL6)
    jeyson6 = res6.json()
    croatian_lamb = jeyson6['meals'][-3]['strMeal']
    croatian_lamb_img = jeyson6['meals'][-3]['strMealThumb']

    # Traditional Croatian Goulash
    API_URL7 = f'https://www.themealdb.com/api/json/v1/1/search.php?f=t'
    res7 = requests.get(API_URL7)
    jeyson7 = res7.json()
    t_croatian = jeyson7['meals'][-1]['strMeal']
    t_croatian_img = jeyson7['meals'][-1]['strMealThumb']

    context = {'chivito':chivito, 'chivito_img':chivito_img, 'walnut':walnut, "walnut_img":walnut_img, 'fresh_sardines_img':fresh_sardines_img, 'fresh_sardines':fresh_sardines, 'burek_img':burek_img,'burek':burek, 'mashroom':mashroom, 'mashroom_img':mashroom_img, 'croatian':croatian, 'croatian_img':croatian_img, 'croatian_lamb':croatian_lamb, 'croatian_lamb_img':croatian_lamb_img, 't_croatian':t_croatian, 't_croatian_img':t_croatian_img, 'all_total_random_ingridients':all_total_random_ingridients, 'all_total':all_total}

    
    return render (request, 'index.html', context=context)



# Filter by Area
def filter_by_area(request, pk):
    total = []
    img = []
    id = []
    if pk == 1:    
        API_URL = f'https://www.themealdb.com/api/json/v1/1/filter.php?a=British'
        res = requests.get(API_URL)
        jeyson = res.json()
        run = len(jeyson['meals'])
        i = 0
        ii = []
        while i != run:
            i=i+1
            ii.append(i)
        ii.insert(0,0)
        ii.pop()
        for y in ii:
            all_meals = jeyson['meals'][y]['strMeal']
            all_img = jeyson['meals'][y]['strMealThumb']
            all_id = jeyson['meals'][y]['idMeal']
            total.append(all_meals)
            img.append(all_img)
            tt = int(all_id)
            id.append(int(tt))
            print(type(tt))
        all_total = zip(img, total, id)
        return render(request, "filter_by_area.html", {'total':all_total})


# Poiskovik 

def search(request):
    if request.method == 'POST':
        searched_product = request.POST.get('search').title()
        total = []
        img = []
        id = []
        all_total = zip(img, total, id)
        API_URL = f'https://www.themealdb.com/api/json/v1/1/search.php?s={searched_product}'
        res = requests.get(API_URL)
        jeyson = res.json()
        run = len(jeyson['meals'])
        i = 0
        ii = []
        while i != run:
            i=i+1
            ii.append(i)
        ii.insert(0,0)
        ii.pop()
        for y in ii:
            all_meals = jeyson['meals'][y]['strMeal']
            all_img = jeyson['meals'][y]['strMealThumb']
            id_meals = jeyson['meals'][y]['idMeal']
            total.append(all_meals)
            img.append(all_img)
            id.append(id_meals)
        return render(request, "search.html", {'total':all_total})
 
def search_ingredients(request):
        if request.method == 'POST':
            searched_product = request.POST.get('search_ingredients').title()
            total = []
            img = []
            id = []
            all_total = zip(img, total, id)
            API_URL = f'http://www.themealdb.com/api/json/v1/1/filter.php?i={searched_product}'
            res = requests.get(API_URL)
            jeyson = res.json()
            run = len(jeyson['meals'])
            i = 0
            ii = []
            while i != run:
                i=i+1
                ii.append(i)
            ii.insert(0,0)
            ii.pop()
            for y in ii:
                all_meals = jeyson['meals'][y]['strMeal']
                id_meals = jeyson['meals'][y]['idMeal']
                all_img = jeyson['meals'][y]['strMealThumb']
                total.append(all_meals)
                img.append(all_img)
                id.append(id_meals)
            return render(request, "search_ingredients.html", {'total':all_total})

# about products
def second_site(request, pk):
    API_URL = f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={pk}'
    res = requests.get(API_URL)
    jeyson = res.json()
    all_is = []
    all_me = []
    name = jeyson['meals'][0]['strMeal']
    iimg = jeyson['meals'][0]['strMealThumb']
    id = jeyson['meals'][0]['idMeal']
    tags = jeyson['meals'][0]['strTags']
    instruction = jeyson['meals'][0]['strInstructions']
    is1 = jeyson['meals'][0]['strIngredient1']
    is2 = jeyson['meals'][0]['strIngredient2']
    is3 = jeyson['meals'][0]['strIngredient3']
    is4 = jeyson['meals'][0]['strIngredient4']
    is5 = jeyson['meals'][0]['strIngredient5']
    is6 = jeyson['meals'][0]['strIngredient6']
    is7 = jeyson['meals'][0]['strIngredient7']
    is8 = jeyson['meals'][0]['strIngredient8']
    is9 = jeyson['meals'][0]['strIngredient9']
    is10 = jeyson['meals'][0]['strIngredient10']
    is11 = jeyson['meals'][0]['strIngredient11']
    is12 = jeyson['meals'][0]['strIngredient12']
    is13 = jeyson['meals'][0]['strIngredient13']
    is14 = jeyson['meals'][0]['strIngredient14']
    is15 = jeyson['meals'][0]['strIngredient15']
    is16 = jeyson['meals'][0]['strIngredient16']
    is17 = jeyson['meals'][0]['strIngredient17']
    is18 = jeyson['meals'][0]['strIngredient18']
    is19 = jeyson['meals'][0]['strIngredient19']
    is20 = jeyson['meals'][0]['strIngredient20']
    me1 = jeyson['meals'][0]['strMeasure1']
    me2 = jeyson['meals'][0]['strMeasure2']
    me3 = jeyson['meals'][0]['strMeasure3']
    me4 = jeyson['meals'][0]['strMeasure4']
    me5 = jeyson['meals'][0]['strMeasure5']
    me6 = jeyson['meals'][0]['strMeasure6']
    me7 = jeyson['meals'][0]['strMeasure7']
    me8 = jeyson['meals'][0]['strMeasure8']
    me9 = jeyson['meals'][0]['strMeasure9']
    me10 = jeyson['meals'][0]['strMeasure10']
    me11 = jeyson['meals'][0]['strMeasure11']
    me12 = jeyson['meals'][0]['strMeasure12']
    me13 = jeyson['meals'][0]['strMeasure13']
    me14 = jeyson['meals'][0]['strMeasure14']
    me15 = jeyson['meals'][0]['strMeasure15']
    me16 = jeyson['meals'][0]['strMeasure16']
    me17 = jeyson['meals'][0]['strMeasure17']
    me18 = jeyson['meals'][0]['strMeasure18']
    me19 = jeyson['meals'][0]['strMeasure19']
    me20 = jeyson['meals'][0]['strMeasure20']
    all_is = [is1, is2,is3, is4, is5,is6,is7,is8,is9,is10,is11,is12,is13,is14,is15,is14,is15,is16,is17, is18,is19, is20]
    all_me = [me1, me2,me3, me4, me5,me6,me7,me8,me9,me10,me11,me12,me13,me14,me15,me14,me15,me16,me17, me18,me19, me20]
    images = []
    while '' in all_is:
        all_me.pop(-1)
        all_is.pop(-1)
        print(all_is)
        print(all_me)
    for imagee in all_is:
        img = f'https://www.themealdb.com/images/ingredients/{imagee}.png'  
        images.append(img)
    gotovka = zip(all_is, all_me, images)
    context = {'name':name, "iimg":iimg, "id":id, 'instruction':instruction, 'tags':tags, 'gotovka':gotovka}
    return render(request, 'index2.html', context=context)

# Authentication



# Список всех блюд по первой букве
def letter(request, pk):
    total = []
    img = []
    id = []
    all_total = zip(img, total,id)
    if pk == 1:    
        API_URL = 'https://www.themealdb.com/api/json/v1/1/search.php?f=a'
        res = requests.get(API_URL)
        jeyson = res.json()
        run = len(jeyson['meals'])
        i = 0
        ii = []
        while i != run:
            i=i+1
            ii.append(i)
        ii.insert(0,0)
        ii.pop()
        for y in ii:
            all_meals = jeyson['meals'][y]['strMeal']
            all_img = jeyson['meals'][y]['strMealThumb']
            all_id = jeyson['meals'][y]['idMeal']
            id.append(all_id)
            total.append(all_meals)
            img.append(all_img)
        return render(request, "letter.html", {'total':all_total})
    elif pk == 2:    
        API_URL = 'https://www.themealdb.com/api/json/v1/1/search.php?f=b'
        res = requests.get(API_URL)
        jeyson = res.json()
        run = len(jeyson['meals'])
        i = 0
        ii = []
        while i != run:
            i=i+1
            ii.append(i)
        ii.insert(0,0)
        ii.pop()
        for y in ii:
            all_meals = jeyson['meals'][y]['strMeal']
            all_img = jeyson['meals'][y]['strMealThumb']
            total.append(all_meals)
            img.append(all_img)   
        return render(request, "letter.html", {'total':all_total})
    elif pk == 3:    
        API_URL = 'https://www.themealdb.com/api/json/v1/1/search.php?f=c'
        res = requests.get(API_URL)
        jeyson = res.json()
        run = len(jeyson['meals'])
        i = 0
        ii = []
        while i != run:
            i=i+1
            ii.append(i)
        ii.insert(0,0)
        ii.pop()
        for y in ii:
            all_meals = jeyson['meals'][y]['strMeal']
            all_img = jeyson['meals'][y]['strMealThumb']
            all_id = jeyson['meals'][y]['idMeal']
            id.append(all_id)
            total.append(all_meals)
            img.append(all_img)   
        return render(request, "letter.html", {'total':all_total})   
    elif pk == 4:    
        API_URL = 'https://www.themealdb.com/api/json/v1/1/search.php?f=d'
        res = requests.get(API_URL)
        jeyson = res.json()
        run = len(jeyson['meals'])
        i = 0
        ii = []
        while i != run:
            i=i+1
            ii.append(i)
        ii.insert(0,0)
        ii.pop()
        for y in ii:
            all_meals = jeyson['meals'][y]['strMeal']
            all_img = jeyson['meals'][y]['strMealThumb']
            all_id = jeyson['meals'][y]['idMeal']
            id.append(all_id)
            total.append(all_meals)
            img.append(all_img)   
        return render(request, "letter.html", {'total':all_total})
    elif pk == 5:    
        API_URL = 'https://www.themealdb.com/api/json/v1/1/search.php?f=e'
        res = requests.get(API_URL)
        jeyson = res.json()
        run = len(jeyson['meals'])
        i = 0
        ii = []
        while i != run:
            i=i+1
            ii.append(i)
        ii.insert(0,0)
        ii.pop()
        for y in ii:
            all_meals = jeyson['meals'][y]['strMeal']
            all_img = jeyson['meals'][y]['strMealThumb']
            all_id = jeyson['meals'][y]['idMeal']
            id.append(all_id)
            total.append(all_meals)
            img.append(all_img)   
        return render(request, "letter.html", {'total':all_total})
        


# res = {}
# def addCart(request, pk):
#     cart_session = request.session.get('cart_session', [])
#     cart_session.append(pk)
#     request.session['cart_session'] = cart_session
#     return redirect('base')





# Basket 
def addToCart(request, id):
    cart_session = request.session.get('cart_session', [])
    cart_session.append(id)
    request.session['cart_session'] = cart_session
    return render(request, 'base.html')

def basket(request):
    cart_session = request.session.get('cart_session', [])
    id = []
    name = []
    img = []
    all_total = zip(name, img, id)
    for i in cart_session:
        API_URL = f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={i}'
        res = requests.get(API_URL)
        jeyson = res.json()
        namee = jeyson['meals'][0]['strMeal']
        iimg = jeyson['meals'][0]['strMealThumb']
        idd = jeyson['meals'][0]['idMeal']
        name.append(namee)
        img.append(iimg)
        id.append(idd)
    return render(request, 'basket.html', {'all_total':all_total})

def removeCart(request ,id):
    cart_session = request.session.get('cart_session', [])
    carts = []
    for pk in cart_session:
        if pk !=id:
            carts.append(pk)
    request.session['cart_session'] = carts
    return redirect('basket')