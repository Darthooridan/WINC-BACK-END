# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#Part 1

def greet(name, greeting_template='Hello, <name>!'):
    return greeting_template.replace('<name>', name)

#Part 2

def force(mass, body='earth'):
    gravities = {
        'sun': 274,
        'mercury': 3.7,
        'venus': 8.87,
        'earth': 9.8,
        'moon': 1.62,
        'mars': 3.71,
        'jupiter': 24.79,
        'saturn': 10.44,
        'uranus': 8.69,
        'neptune': 11.15,
        'pluto': 0.62
    }
    gravity = gravities.get(body.lower(), 9.8)
    gravity = round(gravity, 1)
    return mass * gravity

#Part 3

def pull(m1, m2, d):
    G = 6.674*(10**-11)   
    return G * ((m1 * m2) / d ** 2)


print(pull(800, 1500, 3))
