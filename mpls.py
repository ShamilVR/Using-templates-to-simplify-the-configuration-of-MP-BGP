from jinja2 import Template
import pyperclip

# Шаблон конфигурации интерфейса
interface_template = Template('''
interface {{ interface_name }}
 description {{ description }}
 ip address {{ ip_address }} {{ subnet_mask }}
{{ additional_config }}
''')

# Шаблон конфигурации OSPF
ospf_template = Template('''
router ospf {{ ospf_process_id }}
 network {{ network }} area {{ area }}
''')

# Шаблон конфигурации BGP
bgp_template = Template('''
router bgp {{ bgp_as_number }}
 neighbor {{ neighbor_ip }} remote-as {{ remote_as }}
''')

# Соответствия между сокращениями и полными названиями интерфейсов
interface_mapping = {
    'e': 'ethernet',
    'f': 'fastethernet',
    'g': 'gigabitethernet',
    'l': 'loopback',
    'eth': 'ethernet',
    'fa': 'fastethernet',
    'gi': 'gigabitethernet',
    'lo': 'loopback',
    'ethernet': 'ethernet',
    'fast': 'fastethernet',
    'gig': 'gigabitethernet',
    'loopback': 'loopback',
    'fastethernet': 'fastethernet',
    'gigabitethernet': 'gigabitethernet'
}

# Переменная для хранения конфигурации
full_config = ''

# Функция для проверки и преобразования типа интерфейса
def get_interface_type():
    while True:
        choice = input("Введите сокращение типа интерфейса (e - ethernet, f - fastethernet, g - gigabitethernet, l - loopback): ")
        if choice in interface_mapping:
            return interface_mapping[choice]
        else:
            print("Пожалуйста, выберите сокращение из списка.")

# Функция для проверки ответа пользователя
def get_user_choice(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ['yes', 'no']:
            return choice
        else:
            print("Пожалуйста, введите 'yes' или 'no'.")

# Функция для настройки интерфейса
def configure_interface():
    # Вопросы пользователю
    interface_type = get_interface_type()
    ip_address = input("Введите IP-адрес интерфейса: ")
    subnet_mask_input = input("Введите маску подсети (в формате /24): ")

    # Преобразование маски в формат 255.255.255.0
    subnet_mask_parts = subnet_mask_input.split('/')
    subnet_mask_length = int(subnet_mask_parts[1])
    subnet_mask = '.'.join(['255'] * (subnet_mask_length // 8) + [str(256 - 2**(8 - (subnet_mask_length % 8)))])

    # Входные данные для генерации конфигурации интерфейса
    interface_data = {
        'interface_name': interface_type,
        'description': 'My interface',
        'ip_address': ip_address,
        'subnet_mask': subnet_mask,
        'additional_config': 'no shutdown'
    }

    # Генерация конфигурации интерфейса
    interface_config = interface_template.render(**interface_data)

    # Добавление конфигурации интерфейса к полной конфигурации
    global full_config
    full_config += interface_config + '\n'

    # Проверка, нужно ли настроить OSPF
    ospf_choice = get_user_choice("Хотите настроить OSPF? (yes/no): ")
    if ospf_choice == 'yes':
        configure_ospf()

    # Проверка, нужно ли настроить BGP
    bgp_choice = get_user_choice("Хотите настроить BGP? (yes/no): ")
    if bgp_choice == 'yes':
        configure_bgp()

    # Проверка, нужно ли настроить ещё один интерфейс
    choice = get_user_choice("Хотите настроить ещё один интерфейс? (yes/no): ")
    if choice == 'yes':
        configure_interface()
    else:
        # Сохранение полной конфигурации в буфер обмена
        pyperclip.copy(full_config)
        print("Конфигурация сохранена в буфер обмена.")

# Функция для настройки OSPF
def configure_ospf():
    ospf_process_id = input("Введите номер процесса OSPF: ")
    network = input("Введите сеть OSPF: ")
    area = input("Введите номер области OSPF: ")

    # Входные данные для генерации конфигурации OSPF
    ospf_data = {
        'ospf_process_id': ospf_process_id,
        'network': network,
        'area': area
    }

    # Генерация конфигурации OSPF
    ospf_config = ospf_template.render(**ospf_data)

    # Добавление конфигурации OSPF к полной конфигурации
    global full_config
    full_config += ospf_config + '\n'

# Функция для настройки BGP
def configure_bgp():
    bgp_as_number = input("Введите номер AS BGP: ")
    neighbor_ip = input("Введите IP-адрес соседа BGP: ")
    remote_as = input("Введите номер AS удалённого BGP: ")

    # Входные данные для генерации конфигурации BGP
    bgp_data = {
        'bgp_as_number': bgp_as_number,
        'neighbor_ip': neighbor_ip,
        'remote_as': remote_as
    }

    # Генерация конфигурации BGP
    bgp_config = bgp_template.render(**bgp_data)

    # Добавление конфигурации BGP к полной конфигурации
    global full_config
    full_config += bgp_config + '\n'

# Функция для настройки имени хоста
def configure_hostname():
    hostname = input("Введите имя хоста: ")
    global full_config
    full_config += f"hostname {hostname}\n"

# Начало настройки роутера
configure_hostname()

# Начало настройки интерфейсов
configure_interface()
