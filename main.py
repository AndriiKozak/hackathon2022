from datasource import datasource
import click
@click.command()
@click.option('--name')
@click.option('--surname')
@click.option('--email')
def main(name, surname, email):
    querry = {}
    if name is not None:
        querry["name"] = name
    if surname is not None:
        querry["surname"] = surname
    if email is not None:
        querry["email"] = email
    print(querry)
    print(datasource.query(querry))
if __name__ == '__main__':
    main()
