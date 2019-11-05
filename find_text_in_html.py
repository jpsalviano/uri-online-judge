from bs4 import BeautifulSoup

html = '''		<td>suco de laranja</td>
		<td>120 mg</td>
	</tr>
	<tr>
		<td>morango fresco</td>
		<td>85 mg</td>
	</tr>
	<tr>
		<td>mamao</td>
		<td>85 mg</td>
	</tr>
	<tr>
		<td>goiaba vermelha</td>
		<td>70 mg</td>
	</tr>
	<tr>
		<td>manga</td>
		<td>56 mg</td>
	</tr>
	<tr>
		<td>laranja</td>
		<td>50 mg</td>
	</tr>
	<tr>
		<td>brocolis</td>
		<td>34 mg</td>'''

soup = BeautifulSoup(html, features='html.parser')

ls = soup.find_all('td')
ls_dict = dict()

for i in range(0, len(ls), 2):
    ls_dict[ls[i].text] = ls[i+1].text.replace(' mg', '')
