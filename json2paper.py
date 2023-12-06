import os
import json
import shutil
class Product:
    ith = "0"
    def __init__(self,name,stars,
                  title, desciption, 
                  visit_url, product_hunt_url,
                  comments, my_comment):
        self.name = name
        self.stars = stars
        self.title = title
        self.desciption = desciption
        self.visit_url = visit_url
        self.product_hunt_url = product_hunt_url
        self.comments = comments
        self.my_comment = my_comment

    def set_ith(self, ith):
        self.ith = ith

    def write2md(self, md_file):
        f = open(md_file, 'a')
        f.write("## " + self.ith + "."+ self.name )
        f.write("\n\n")
        f.write("点赞量 " + self.stars)
        f.write("\n\n")
        f.write("> ---" + self.title )
        f.write("\n\n")
        f.write(self.desciption )
        f.write("\n\n")
        f.write("[点击尝试{0}]({1})".format(self.title, self.visit_url))
        f.write("\n\n")
        f.write("[product hunt点评]({0})".format(self.product_hunt_url))
        f.write("\n\n")
        for commentor in self.comments:
            comment = self.comments[commentor]
            f.write("> {0}:".format(commentor))
            f.write("\n")
            f.write("> {0}".format(comment))
            f.write("\n\n")
        f.write("我的看法:{0}".format(self.my_comment))
        f.write("\n\n")
        f.close()

class Paper:
    output_file = "./output.md"
    def __init__(self, paper_name, date, products):
        self.paper_name = paper_name
        self.date = date
        self.products = products
    def write2md(self):
        if (os.path.exists(self.output_file)):
            os.remove(self.output_file)
        f = open(self.output_file, 'w')
        f.write("# " +self.paper_name + " " + self.date[5:] + " product hunt")
        f.write("\n\n")
        f.close()
        for (ith, product) in enumerate(self.products):
            product.set_ith(str(ith+1))
            product.write2md(self.output_file)
        
        #save to dir
        directory = self.date
        parent_dir = "./"
        dir_path = os.path.join(parent_dir, directory)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file_path = os.path.join(dir_path, self.paper_name)
        if (os.path.exists(file_path)):
            os.remove(file_path)
        shutil.copy(self.output_file, dir_path)

def json2paper(input_file = "input.json"):
    with open(input_file) as json_file:
        input_data = json.load(json_file)
    #extract products
    products = []
    for product_dict in input_data["products"]:
        name = product_dict["name"]
        stars = product_dict["stars"]
        title = product_dict["title"]
        description = product_dict["description"]
        visit_url = product_dict["visit_url"]
        product_hunt_url = product_dict["product_hunt_url"]
        comments = product_dict["comments"]
        my_comment = product_dict["my_comment"]
        products.append(Product(name, stars, title, description, visit_url, product_hunt_url, comments, my_comment))
    #extract paper
    paper_name = input_data["paper_name"]
    date = input_data["date"]
    return Paper(paper_name, date, products)

paper = json2paper()
paper.write2md()

