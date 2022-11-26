from abc import abstractmethod
from typing import List, Dict


class DataSource:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def query(self, params: Dict) -> Dict:
        pass


class PlainTextDataSource(DataSource):
    def __init__(self, paths: List[str], keys: List[str], delimeter=" ", encoding="UTF-8", debug=False):
        self.paths = paths
        self.keys = keys
        self.delimeter = delimeter
        self.encoding = encoding
        self.debug = debug

    def query(self, params):
        result = dict()
        if len(set(self.keys).intersection(params.keys())) == 0:
            return result
        for path in self.paths:
            with open(path, "r", encoding=self.encoding) as file:
                for line in file:
                    values = line[:-1].split(self.delimeter)
                    for key, value in params.items():
                        try:
                            if values[self.keys.index(key)] != value:
                                break
                        except ValueError:
                            continue
                        except IndexError:
                            if self.debug:
                                print("index error!!!", key, self.keys, value, values)
                            break
                    else:
                        result.update(**{key: value for key, value in zip(self.keys, values)})
        return result


class CompositeDatasource(DataSource):
    def __init__(self, datasources: List[DataSource]):
        self.datasources = datasources

    def query(self, params: Dict) -> Dict:
        result = dict()
        for datasource in self.datasources:
            result.update(datasource.query(params))
        return result


datasource = CompositeDatasource([
    PlainTextDataSource(["D:/db/Умное голосования.csv"], ["SNP", "birthday", "email", "phone"], delimeter=";"),
    PlainTextDataSource(["D:/db/VK 2022/1.csv", "D:/db/VK 2022/2.csv", "D:/db/VK 2022/3.csv"],
                        ["vk_id", "vk_url", "name", "surname", "sex", "birthday", "age", "country", "city", "instagram",
                         "phone"], delimeter=";", debug=True),
    PlainTextDataSource(["D:/db/artnow_users.csv"],
                        ["artnow_id", "artnow_login", "artnow_pswd", "artnow_nick", "email", "phone", "city",
                         "country"], delimeter=","),
    PlainTextDataSource(["D:/db/avtoto.csv/avtoto.csv"], ["phone", "SNP", "email", "adress", "avtototo password"],
                        delimeter="\t"),
    #PlainTextDataSource(["D:db/cdek/cdek/client.csv"], ["cdek_id",	"cdek_contract_number",	"SNP",	"contact_person SNP",	"address_id",	"cdek_pickup_point_code",	"email"])
])
