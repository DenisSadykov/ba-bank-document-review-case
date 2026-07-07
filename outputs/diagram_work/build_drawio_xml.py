from xml.sax.saxutils import escape

cells = []
cell_id = 2
edge_id = 1000

def add_vertex(value, x, y, w, h, style, parent='1'):
    global cell_id
    cid = str(cell_id)
    cell_id += 1
    cells.append(f'<mxCell id="{cid}" value="{escape(value)}" style="{style}" vertex="1" parent="{parent}"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    return cid

def add_edge(source, target, style, points=None, parent='1'):
    global edge_id
    cid = str(edge_id)
    edge_id += 1
    if points:
        pts = ''.join([f'<mxPoint x="{x}" y="{y}"/>' for x,y in points])
        geom = f'<mxGeometry relative="1" as="geometry"><Array as="points">{pts}</Array></mxGeometry>'
    else:
        geom = '<mxGeometry relative="1" as="geometry"/>'
    cells.append(f'<mxCell id="{cid}" style="{style}" edge="1" parent="{parent}" source="{source}" target="{target}">{geom}</mxCell>')
    return cid

def add_label(value, x, y, w, h):
    global cell_id
    cid = str(cell_id)
    cell_id += 1
    style = 'text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontSize=16;fontColor=#334155;fontStyle=0;'
    cells.append(f'<mxCell id="{cid}" value="{escape(value)}" style="{style}" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    return cid

blue = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#F8FBFF;strokeColor=#2F80ED;strokeWidth=2;fontColor=#19324D;fontSize=18;fontStyle=1;align=center;verticalAlign=middle;spacing=8;arcSize=14;'
blue_small = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#F8FBFF;strokeColor=#2F80ED;strokeWidth=2;fontColor=#19324D;fontSize=16;fontStyle=1;align=center;verticalAlign=middle;spacing=8;arcSize=14;'
red = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF4F4;strokeColor=#EB5757;strokeWidth=2;fontColor=#19324D;fontSize=16;fontStyle=1;align=center;verticalAlign=middle;spacing=8;arcSize=14;'
green = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#F1FBF4;strokeColor=#27AE60;strokeWidth=2;fontColor=#19324D;fontSize=16;fontStyle=1;align=center;verticalAlign=middle;spacing=8;arcSize=14;'
yellow = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF9EB;strokeColor=#F2C94C;strokeWidth=2;fontColor=#19324D;fontSize=16;fontStyle=1;align=center;verticalAlign=middle;spacing=8;arcSize=14;'
diamond = 'rhombus;whiteSpace=wrap;html=1;fillColor=#FFFAF2;strokeColor=#F2994A;strokeWidth=2;fontColor=#19324D;fontSize=18;fontStyle=1;align=center;verticalAlign=middle;spacing=8;'
edge = 'edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#7A8797;strokeWidth=2;endArrow=block;endFill=1;'
arrow = 'edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4A5568;strokeWidth=2.5;endArrow=block;endFill=1;'

title_style = 'text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontSize=28;fontColor=#19324D;fontStyle=1;'
subtitle_style = 'text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontSize=18;fontColor=#19324D;fontStyle=1;'

# title
cells.append(f'<mxCell id="title" value="{escape("Процесс первичной проверки пакета документов")}" style="{title_style}" vertex="1" parent="1"><mxGeometry x="310" y="20" width="1180" height="40" as="geometry"/></mxCell>')
cells.append(f'<mxCell id="subtitle" value="{escape("Перед заявлением авансового платежа в банк")}" style="{subtitle_style}" vertex="1" parent="1"><mxGeometry x="500" y="62" width="800" height="28" as="geometry"/></mxCell>')

start = add_vertex('Старт', 690, 120, 420, 70, blue)
upload = add_vertex('Специалист загружает пакет документов\n\nдоговор, спецификация, счет, УПД/акт, правила программы', 520, 240, 760, 105, blue)
program = add_vertex('Выбор льготной программы\n\nфедеральная / областная', 590, 395, 620, 92, blue)
extract = add_vertex('AI-агент извлекает данные из документов\n\nконтрагент, сумма, даты, предмет оплаты, номенклатура, количество,\nсроки, ссылки на приложения, признаки подписи и печати', 430, 540, 940, 115, blue_small)
complete = add_vertex('Проверка комплектности пакета\n\nвсе ли обязательные документы приложены', 575, 705, 650, 92, blue)
d1 = add_vertex('Есть обязательный документ,\nкоторого не хватает?', 610, 850, 580, 210, diamond)
status1 = add_vertex('Статус: Нельзя заявлять\n\nПричина: неполный комплект', 90, 980, 360, 100, red)
check = add_vertex('Проверка реквизитов и правил программы\n\nсроки, соответствие предмета оплаты, обязательные реквизиты,\nсвязность договора, спецификации и счета, наличие подписи/печати', 390, 1125, 1020, 110, blue_small)
d2 = add_vertex('Найден критичный\nстоп-фактор?', 610, 1290, 580, 200, diamond)
status2 = add_vertex('Статус: Нельзя заявлять\n\nПричина: найдено нарушение', 90, 1420, 360, 100, red)
d3 = add_vertex('Есть сомнение,\nнизкая уверенность\nили неполные данные?', 1110, 1465, 420, 180, diamond)
status_ok = add_vertex('Статус: Можно заявлять в банк\n\nВсе обязательные проверки пройдены', 210, 1725, 620, 105, green)
status_manual = add_vertex('Статус: Требуется ручная проверка\n\nКейс передается специалисту / контролеру', 980, 1725, 560, 105, yellow)

# main flow
for a,b in [(start,upload),(upload,program),(program,extract),(extract,complete),(complete,d1),(d1,check),(check,d2)]:
    add_edge(a,b,arrow)

# branches from d1
add_edge(d1,status1,edge,points=[(350,955),(270,955),(270,980)])
add_label('Да', 335, 905, 50, 24)
add_edge(d1,check,edge,points=[(1370,955),(1430,955),(1430,1180),(1410,1180)])
add_label('Нет', 1235, 905, 50, 24)

# branches from d2
add_edge(d2,status2,edge,points=[(350,1390),(270,1390),(270,1420)])
add_label('Да', 335, 1340, 50, 24)
add_edge(d2,d3,edge,points=[(1310,1390),(1310,1465)])
add_label('Нет', 1215, 1340, 50, 24)

# branches from d3
add_edge(d3,status_ok,edge,points=[(1040,1555),(540,1555),(540,1725)])
add_label('Нет', 700, 1510, 60, 24)
add_edge(d3,status_manual,edge,points=[(1540,1555),(1540,1725)])
add_label('Да', 1500, 1510, 45, 24)

xml = f'''<mxGraphModel dx="1436" dy="827" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1800" pageHeight="2300" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    {''.join(cells)}
  </root>
</mxGraphModel>'''

open('outputs/diagram_work/process_scheme_mxgraph.xml', 'w', encoding='utf-8').write(xml)
print('written outputs/diagram_work/process_scheme_mxgraph.xml')
