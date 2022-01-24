from logging import error
from turtle import home
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

null = None


class home_(Resource):
    def get(self):
        return {
            "data": [
                {
                    "header": [
                        {
                            "navbar": [
                                {
                                    "logo": {
                                        "text": "PEXMAN CREATIVE AGENCY",
                                        "url": "https://preview.colorlib.com/theme/pexman/index.html"
                                    }
                                },
                                {
                                    "Menu": [
                                        {
                                            "text": "HOME",
                                            "url": "https://preview.colorlib.com/theme/pexman/index.html"
                                        },
                                        {
                                            "text": "ABOUT",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html"
                                        },
                                        {
                                            "text": "WORKS",
                                            "url": "https://preview.colorlib.com/theme/pexman/work.html"
                                        },
                                        {
                                            "text": "BLOG",
                                            "url": "https://preview.colorlib.com/theme/pexman/blog.html"
                                        },
                                        {
                                            "text": "CONTACT",
                                            "url": "https://preview.colorlib.com/theme/pexman/contact.html"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "carousel": [
                                {
                                    "img": "images/xbg_1.jpg.pagespeed.ic.Ojq-dWQTjg.webp",
                                    "judul": "Build Stunning Websites Design",
                                    "subjudul": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth.",
                                    "button": {
                                        "url": "https://preview.colorlib.com/theme/pexman/index.html#",
                                        "text": "View Portfolio",
                                        "icon": "ion ion-ios-arrow-round-forward"
                                    }
                                },
                                {
                                    "img": "images/xbg_2.jpg.pagespeed.ic.-koteA0VFn.webp",
                                    "judul": "Make Creative Website",
                                    "subjudul": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth.",
                                    "button": {
                                        "url": "https://preview.colorlib.com/theme/pexman/index.html#",
                                        "text": "View Portfolio",
                                        "icon": "ion ion-ios-arrow-round-forward"
                                    }
                                },
                                {
                                    "img": "images/xbg_3.jpg.pagespeed.ic.oT_FzzcNOf.webp",
                                    "judul": "We Are Pexman Creative Agency",
                                    "subjudul": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth.",
                                    "button": {
                                        "url": "https://preview.colorlib.com/theme/pexman/index.html#",
                                        "text": "View Portfolio",
                                        "icon": "ion ion-ios-arrow-round-forward"
                                    }
                                },
                                {
                                    "thumbnail": [
                                        {
                                            "text": "01.",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "text": "01.",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "text": "01.",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "main": [
                        {
                            "Welcome": [
                                {
                                    "background": {
                                        "img": "images/xabout.jpg.pagespeed.ic.8p3LFl59dX.webp"
                                    }
                                },
                                {
                                    "pembukaan": [
                                        {
                                            "subHeading": "WELCOME PEXMAN",
                                            "judul": "We Are Creative Agency That Create Beautiful Websites",
                                            "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.",
                                            "button": {
                                                "text": "Start A Project",
                                                "url": "https://preview.colorlib.com/theme/pexman/index.html#",
                                                "icon": "ion ion-ios-arrow-round-forward"
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "rating": [
                                {
                                    "background": {
                                        "img": "images/xbg_1.jpg.pagespeed.ic.Ojq-dWQTjg.webp"
                                    }
                                },
                                {
                                    "isiRating": [
                                        {
                                            "number": "10",
                                            "subNumber": "K+",
                                            "text": "ACHIEVEMENTS"
                                        },
                                        {
                                            "number": "21",
                                            "subNumber": "K+",
                                            "text": "PROJECT COMPLETED"
                                        },
                                        {
                                            "number": "27",
                                            "text": "YEARS OF EXPERIENCED"
                                        },
                                        {
                                            "number": "30",
                                            "subNumber": "K+",
                                            "text": "HAPPY CUSTOMERS"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "What We Offer": [
                                {
                                    "gambar": {
                                        "img": "images/xabout-2.jpg.pagespeed.ic.TYyF1H_gUC.webp"
                                    }
                                },
                                {
                                    "heading": {
                                        "subHeading": "WHAT WE OFFER",
                                        "judul": "What We Offer",
                                        "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                    }
                                },
                                {
                                    "isi konten": [
                                        {
                                            "number": "1",
                                            "title": "Research",
                                            "text": "A small river named Duden flows by their place."
                                        },
                                        {
                                            "number": "2",
                                            "title": "Design",
                                            "text": "A small river named Duden flows by their place."
                                        },
                                        {
                                            "number": "3",
                                            "title": "Development",
                                            "text": "A small river named Duden flows by their place."
                                        },
                                        {
                                            "number": "4",
                                            "title": "Testing",
                                            "text": "A small river named Duden flows by their place."
                                        },
                                        {
                                            "url": "https://preview.colorlib.com/theme/pexman/#",
                                            "text": "Start A Project",
                                            "icon": "ion ion-ios-arrow-round-forward"
                                        }
                                    ]
                                },
                                {
                                    "kemampuan": [
                                        {
                                            "judul": "Web Design",
                                            "text": "A small river named Duden flows by their place and supplies it with the necessary regelialia.",
                                            "icon": "flaticon-computer"
                                        },
                                        {
                                            "judul": "Phortography",
                                            "text": "A small river named Duden flows by their place and supplies it with the necessary regelialia.",
                                            "icon": "flaticon-camera"
                                        },
                                        {
                                            "judul": "Marketing",
                                            "text": "A small river named Duden flows by their place and supplies it with the necessary regelialia.",
                                            "icon": "flaticon-bullhorn"
                                        },
                                        {
                                            "judul": "Graphic Design",
                                            "text": "A small river named Duden flows by their place and supplies it with the necessary regelialia.",
                                            "icon": "flaticon-vector"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "Our Portofolio": [
                                {
                                    "heading": {
                                        "subHeading": "OUR PORTFOLIO",
                                        "judul": "Our Stunning Works"
                                    }
                                },
                                {
                                    "menu": [
                                        {
                                            "text": "ALL",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "text": "BRANDING",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "text": "WEB DESIGN",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "text": "ILLUSTRATION",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "text": "APPLICATION",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                        }
                                    ]
                                },
                                {
                                    "isiportofolio": [
                                        {
                                            "img": "images/xwork-1.jpg.pagespeed.ic.3j7JGYqbGF.webp",
                                            "judul": "Hark Website",
                                            "subJudul": "WEB DESIGN,BRANDING",
                                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                            "icon": "fa fa-search"
                                        },
                                        {
                                            "img": "images/xwork-2.jpg.pagespeed.ic.10n42M66q2.webp",
                                            "judul": "Hark Website",
                                            "subJudul": "WEB DESIGN,BRANDING",
                                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                            "icon": "fa fa-search"
                                        },
                                        {
                                            "img": "images/xwork-3.jpg.pagespeed.ic.RnZ9RkAZUD.webp",
                                            "judul": "Hark Website",
                                            "subJudul": "WEB DESIGN,BRANDING",
                                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                            "icon": "fa fa-search"
                                        },
                                        {
                                            "img": "images/xwork-4.jpg.pagespeed.ic.RrfN8RD85H.webp",
                                            "judul": "Hark Website",
                                            "subJudul": "WEB DESIGN,BRANDING",
                                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                            "icon": "fa fa-search"
                                        },
                                        {
                                            "img": "images/xwork-5.jpg.pagespeed.ic.tS4bFn-pmq.webp",
                                            "judul": "Hark Website",
                                            "subJudul": "WEB DESIGN,BRANDING",
                                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                            "icon": "fa fa-search"
                                        },
                                        {
                                            "img": "images/xwork-6.jpg.pagespeed.ic.RupLEjxNLP.webp",
                                            "judul": "Hark Website",
                                            "subJudul": "WEB DESIGN,BRANDING",
                                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                            "icon": "fa fa-search"
                                        },
                                        {
                                            "img": "images/xwork-7.jpg.pagespeed.ic.VL2SUY_RpS.webp",
                                            "judul": "Hark Website",
                                            "subJudul": "WEB DESIGN,BRANDING",
                                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                            "icon": "fa fa-search"
                                        },
                                        {
                                            "img": "images/xwork-8.jpg.pagespeed.ic.BEEvFj7ItC.webp",
                                            "judul": "Hark Website",
                                            "subJudul": "WEB DESIGN,BRANDING",
                                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                            "icon": "fa fa-search"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "testimoni": [
                                {
                                    "subHeading": {
                                        "text": "TESTIMONIAL"
                                    }
                                },
                                {
                                    "subTitle": {
                                        "text": "What Are Clients Says"
                                    }
                                },
                                {
                                    "testi1": [
                                        {
                                            "fotoTesti": {
                                                "img": "images/xperson_1.jpg.pagespeed.ic.a2MnMHMs44.webp"
                                            }
                                        },
                                        {
                                            "bintang": {
                                                "icon": "fa fa-star"
                                            }
                                        },
                                        {
                                            "isiTesti": {
                                                "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                            }
                                        },
                                        {
                                            "namaTesti": {
                                                "text": "Roger Scott"
                                            }
                                        },
                                        {
                                            "position": {
                                                "text": "Cheif Executive Officer @pexman"
                                            }
                                        }
                                    ]
                                },
                                {
                                    "testi2": [
                                        {
                                            "fotoTesti": {
                                                "img": "images/xperson_2.jpg.pagespeed.ic.Xrdu_nPZRp.webp"
                                            }
                                        },
                                        {
                                            "bintang": {
                                                "icon": "fa fa-star"
                                            }
                                        },
                                        {
                                            "isiTesti": {
                                                "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                            }
                                        },
                                        {
                                            "namaTesti": {
                                                "text": "Roger Scott"
                                            }
                                        },
                                        {
                                            "position": {
                                                "text": "Cheif Executive Officer @pexman"
                                            }
                                        }
                                    ]
                                },
                                {
                                    "testi3": [
                                        {
                                            "fotoTesti": {
                                                "img": "images/xperson_3.jpg.pagespeed.ic.Cln-jaM1jK.webp"
                                            }
                                        },
                                        {
                                            "bintang": {
                                                "icon": "fa fa-star"
                                            }
                                        },
                                        {
                                            "isiTesti": {
                                                "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                            }
                                        },
                                        {
                                            "namaTesti": {
                                                "text": "Roger Scott"
                                            }
                                        },
                                        {
                                            "position": {
                                                "text": "Cheif Executive Officer @pexman"
                                            }
                                        }
                                    ]
                                },
                                {
                                    "testi4": [
                                        {
                                            "fotoTesti": {
                                                "img": "images/xperson_4.jpg.pagespeed.ic.ucbtJ1Htlo.webp"
                                            }
                                        },
                                        {
                                            "bintang": {
                                                "icon": "fa fa-star"
                                            }
                                        },
                                        {
                                            "isiTesti": {
                                                "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                            }
                                        },
                                        {
                                            "namaTesti": {
                                                "text": "Roger Scott"
                                            }
                                        },
                                        {
                                            "position": {
                                                "text": "Cheif Executive Officer @pexman"
                                            }
                                        }
                                    ]
                                },
                                {
                                    "testi5": [
                                        {
                                            "fotoTesti": {
                                                "img": "images/xperson_2.jpg.pagespeed.ic.Xrdu_nPZRp.webp"
                                            }
                                        },
                                        {
                                            "bintang": {
                                                "icon": "fa fa-star"
                                            }
                                        },
                                        {
                                            "isiTesti": {
                                                "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                            }
                                        },
                                        {
                                            "namaTesti": {
                                                "text": "Roger Scott"
                                            }
                                        },
                                        {
                                            "position": {
                                                "text": "Cheif Executive Officer @pexman"
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "Read Latest News": [
                                {
                                    "heading": {
                                        "subHeading": "READ LATEST NEWS",
                                        "textjudul": "Our Latest Blog"
                                    }
                                },
                                {
                                    "isi Red Latest News": [
                                        {
                                            "img": "images/ximage_1.jpg.pagespeed.ic.FL0iBhryhq.webp",
                                            "url": "https://preview.colorlib.com/theme/pexman/blog-single.html",
                                            "icon": "fa fa-calendar",
                                            "textTanggal": "Oct. 27, 2020",
                                            "title": "Far far away, behind the word mountains",
                                            "textIsi": "Far far away, behind the word mountains, far from the countries.",
                                            "urlJudul": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "img": "images/ximage_2.jpg.pagespeed.ic.-x0Ll8ptzk.webp",
                                            "urlimg": "https://preview.colorlib.com/theme/pexman/blog-single.html",
                                            "icon": "fa fa-calendar",
                                            "textTanggal": "Oct. 27, 2020",
                                            "title": "Far far away, behind the word mountains",
                                            "textIsi": "Far far away, behind the word mountains, far from the countries.",
                                            "urlJudul": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "img": "images/ximage_3.jpg.pagespeed.ic.DwkWtPATES.webp",
                                            "urlimg": "https://preview.colorlib.com/theme/pexman/blog-single.html",
                                            "icon": "fa fa-calendar",
                                            "textTanggal": "Oct. 27, 2020",
                                            "title": "Far far away, behind the word mountains",
                                            "textIsi": "Far far away, behind the word mountains, far from the countries.",
                                            "urlJudul": "https://preview.colorlib.com/theme/pexman/#"
                                        },
                                        {
                                            "img": "images/ximage_4.jpg.pagespeed.ic.r0BKEhAIc3.webp",
                                            "urlimg": "https://preview.colorlib.com/theme/pexman/blog-single.html",
                                            "icon": "fa fa-calendar",
                                            "textTanggal": "Oct. 27, 2020",
                                            "title": "Far far away, behind the word mountains",
                                            "textIsi": "Far far away, behind the word mountains, far from the countries.",
                                            "urlJudul": "https://preview.colorlib.com/theme/pexman/#"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "footer": [
                        {
                            "Pexman": [
                                {
                                    "textJudul": "Pexman",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                }
                            ]
                        },
                        {
                            "connect With Us": [
                                {
                                    "textJudul": "Connect with us"
                                },
                                {
                                    "icon": "fa fa-twitter",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "icon": "fa fa-facebook",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "icon": "fa fa-instagram",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                }
                            ]
                        },
                        {
                            "Navigation": [
                                {
                                    "textJudul": "Navigation"
                                },
                                {
                                    "text": "Home",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "text": "Work",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "text": "About",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "text": "Blog",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "text": "Press",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "text": "Blog",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "text": "Contact",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "text": "Support",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "text": "Privacy",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                }
                            ]
                        },
                        {
                            "Have a Question": [
                                {
                                    "textJudul": "Have a Question?"
                                },
                                {
                                    "icon": "fa fa-map marker",
                                            "text": "203 Fake St. Mountain View, San Francisco, California, USA"
                                },
                                {
                                    "icon": "fa fa-phone",
                                            "text": "+2 392 3929 210",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "icon": "fa fa-paper-plane",
                                            "text": "info@yourdomain.com",
                                            "url": "https://preview.colorlib.com/theme/pexman/#"
                                }
                            ]
                        },
                        {
                            "akhir": {
                                "text": "Copyright ©2022 All rights reserved | This template is made with  by Colorlib",
                                        "url": "https://colorlib.com/",
                                        "icon": "fa fa-heart"
                            }
                        }
                    ]
                }
            ]
        }


class home_navbar(Resource):
    def get(self):
        return {
            "data": [
                {
                    "navbar": [
                        {
                            "logo": {
                                "text": "PEXMAN CREATIVE AGENCY",
                                        "url": "https://preview.colorlib.com/theme/pexman/index.html"
                            }
                        },
                        {
                            "Menu": [
                                {
                                    "text": "HOME",
                                            "url": "https://preview.colorlib.com/theme/pexman/index.html"
                                },
                                {
                                    "text": "ABOUT",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html"
                                },
                                {
                                    "text": "WORKS",
                                            "url": "https://preview.colorlib.com/theme/pexman/work.html"
                                },
                                {
                                    "text": "BLOG",
                                            "url": "https://preview.colorlib.com/theme/pexman/blog.html"
                                },
                                {
                                    "text": "CONTACT",
                                            "url": "https://preview.colorlib.com/theme/pexman/contact.html"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class home_carousel(Resource):
    def get(self):
        return {
            "data": [
                {
                    "carousel": [
                        {
                            "img": "images/xbg_1.jpg.pagespeed.ic.Ojq-dWQTjg.webp",
                            "judul": "Build Stunning Websites Design",
                            "subjudul": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth.",
                            "button": {
                                "url": "https://preview.colorlib.com/theme/pexman/index.html#",
                                "text": "View Portfolio",
                                "icon": "ion ion-ios-arrow-round-forward"
                            }
                        },
                        {
                            "img": "images/xbg_2.jpg.pagespeed.ic.-koteA0VFn.webp",
                            "judul": "Make Creative Website",
                            "subjudul": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth.",
                            "button": {
                                "url": "https://preview.colorlib.com/theme/pexman/index.html#",
                                "text": "View Portfolio",
                                "icon": "ion ion-ios-arrow-round-forward"
                            }
                        },
                        {
                            "img": "images/xbg_3.jpg.pagespeed.ic.oT_FzzcNOf.webp",
                            "judul": "We Are Pexman Creative Agency",
                            "subjudul": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth.",
                            "button": {
                                "url": "https://preview.colorlib.com/theme/pexman/index.html#",
                                "text": "View Portfolio",
                                "icon": "ion ion-ios-arrow-round-forward"
                            }
                        },
                        {
                            "thumbnail": [
                                {
                                    "text": "01.",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "text": "01.",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "text": "01.",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class home_welcome(Resource):
    def get(self):
        return {
            "data": [


                {
                    "Welcome": [
                        {
                            "background": {
                                "img": "images/xabout.jpg.pagespeed.ic.8p3LFl59dX.webp"
                            }
                        },
                        {
                            "pembukaan": [
                                {
                                    "subHeading": "WELCOME PEXMAN",
                                    "judul": "We Are Creative Agency That Create Beautiful Websites",
                                    "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.",
                                    "button": {
                                        "text": "Start A Project",
                                        "url": "https://preview.colorlib.com/theme/pexman/index.html#",
                                        "icon": "ion ion-ios-arrow-round-forward"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class home_rating(Resource):
    def get(self):
        return {
            "data": [
                {
                    "rating": [
                        {
                            "background": {
                                "img": "images/xbg_1.jpg.pagespeed.ic.Ojq-dWQTjg.webp"
                            }
                        },
                        {
                            "isiRating": [
                                {
                                    "number": "10",
                                    "subNumber": "K+",
                                    "text": "ACHIEVEMENTS"
                                },
                                {
                                    "number": "21",
                                    "subNumber": "K+",
                                    "text": "PROJECT COMPLETED"
                                },
                                {
                                    "number": "27",
                                    "text": "YEARS OF EXPERIENCED"
                                },
                                {
                                    "number": "30",
                                    "subNumber": "K+",
                                    "text": "HAPPY CUSTOMERS"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class home_What_We_Offer(Resource):
    def get(self):
        return {
            "data": [
                {
                    "What We Offer": [
                        {
                            "gambar": {
                                "img": "images/xabout-2.jpg.pagespeed.ic.TYyF1H_gUC.webp"
                            }
                        },
                        {
                            "heading": {
                                "subHeading": "WHAT WE OFFER",
                                "judul": "What We Offer",
                                "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                            }
                        },
                        {
                            "isi konten": [
                                {
                                    "number": "1",
                                    "title": "Research",
                                    "text": "A small river named Duden flows by their place."
                                },
                                {
                                    "number": "2",
                                    "title": "Design",
                                    "text": "A small river named Duden flows by their place."
                                },
                                {
                                    "number": "3",
                                    "title": "Development",
                                    "text": "A small river named Duden flows by their place."
                                },
                                {
                                    "number": "4",
                                    "title": "Testing",
                                    "text": "A small river named Duden flows by their place."
                                },
                                {
                                    "url": "https://preview.colorlib.com/theme/pexman/#",
                                    "text": "Start A Project",
                                    "icon": "ion ion-ios-arrow-round-forward"
                                }
                            ]
                        },
                        {
                            "kemampuan": [
                                {
                                    "judul": "Web Design",
                                    "text": "A small river named Duden flows by their place and supplies it with the necessary regelialia.",
                                    "icon": "flaticon-computer"
                                },
                                {
                                    "judul": "Phortography",
                                    "text": "A small river named Duden flows by their place and supplies it with the necessary regelialia.",
                                    "icon": "flaticon-camera"
                                },
                                {
                                    "judul": "Marketing",
                                    "text": "A small river named Duden flows by their place and supplies it with the necessary regelialia.",
                                    "icon": "flaticon-bullhorn"
                                },
                                {
                                    "judul": "Graphic Design",
                                    "text": "A small river named Duden flows by their place and supplies it with the necessary regelialia.",
                                    "icon": "flaticon-vector"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class home_Our_Portofolio(Resource):
    def get(self):
        return {
            "data": [
                {
                    "Our Portofolio": [
                        {
                            "heading": {
                                "subHeading": "OUR PORTFOLIO",
                                "judul": "Our Stunning Works"
                            }
                        },
                        {
                            "menu": [
                                {
                                    "text": "ALL",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "text": "BRANDING",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "text": "WEB DESIGN",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "text": "ILLUSTRATION",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "text": "APPLICATION",
                                    "url": "https://preview.colorlib.com/theme/pexman/#"
                                }
                            ]
                        },
                        {
                            "isiportofolio": [
                                {
                                    "img": "images/xwork-1.jpg.pagespeed.ic.3j7JGYqbGF.webp",
                                    "judul": "Hark Website",
                                    "subJudul": "WEB DESIGN,BRANDING",
                                    "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                    "icon": "fa fa-search"
                                },
                                {
                                    "img": "images/xwork-2.jpg.pagespeed.ic.10n42M66q2.webp",
                                    "judul": "Hark Website",
                                    "subJudul": "WEB DESIGN,BRANDING",
                                    "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                    "icon": "fa fa-search"
                                },
                                {
                                    "img": "images/xwork-3.jpg.pagespeed.ic.RnZ9RkAZUD.webp",
                                    "judul": "Hark Website",
                                    "subJudul": "WEB DESIGN,BRANDING",
                                    "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                    "icon": "fa fa-search"
                                },
                                {
                                    "img": "images/xwork-4.jpg.pagespeed.ic.RrfN8RD85H.webp",
                                    "judul": "Hark Website",
                                    "subJudul": "WEB DESIGN,BRANDING",
                                    "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                    "icon": "fa fa-search"
                                },
                                {
                                    "img": "images/xwork-5.jpg.pagespeed.ic.tS4bFn-pmq.webp",
                                    "judul": "Hark Website",
                                    "subJudul": "WEB DESIGN,BRANDING",
                                    "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                    "icon": "fa fa-search"
                                },
                                {
                                    "img": "images/xwork-6.jpg.pagespeed.ic.RupLEjxNLP.webp",
                                    "judul": "Hark Website",
                                    "subJudul": "WEB DESIGN,BRANDING",
                                    "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                    "icon": "fa fa-search"
                                },
                                {
                                    "img": "images/xwork-7.jpg.pagespeed.ic.VL2SUY_RpS.webp",
                                    "judul": "Hark Website",
                                    "subJudul": "WEB DESIGN,BRANDING",
                                    "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                    "icon": "fa fa-search"
                                },
                                {
                                    "img": "images/xwork-8.jpg.pagespeed.ic.BEEvFj7ItC.webp",
                                    "judul": "Hark Website",
                                    "subJudul": "WEB DESIGN,BRANDING",
                                    "url": "https://preview.colorlib.com/theme/pexman/work.html",
                                    "icon": "fa fa-search"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class home_testimoni(Resource):
    def get(self):
        return {
            "data": [
                {
                    "testimoni": [
                        {
                            "subHeading": {
                                "text": "TESTIMONIAL"
                            }
                        },
                        {
                            "subTitle": {
                                "text": "What Are Clients Says"
                            }
                        },
                        {
                            "testi1": [
                                {
                                    "fotoTesti": {
                                        "img": "images/xperson_1.jpg.pagespeed.ic.a2MnMHMs44.webp"
                                    }
                                },
                                {
                                    "bintang": {
                                        "icon": "fa fa-star"
                                    }
                                },
                                {
                                    "isiTesti": {
                                        "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                    }
                                },
                                {
                                    "namaTesti": {
                                        "text": "Roger Scott"
                                    }
                                },
                                {
                                    "position": {
                                        "text": "Cheif Executive Officer @pexman"
                                    }
                                }
                            ]
                        },
                        {
                            "testi2": [
                                {
                                    "fotoTesti": {
                                        "img": "images/xperson_2.jpg.pagespeed.ic.Xrdu_nPZRp.webp"
                                    }
                                },
                                {
                                    "bintang": {
                                        "icon": "fa fa-star"
                                    }
                                },
                                {
                                    "isiTesti": {
                                        "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                    }
                                },
                                {
                                    "namaTesti": {
                                        "text": "Roger Scott"
                                    }
                                },
                                {
                                    "position": {
                                        "text": "Cheif Executive Officer @pexman"
                                    }
                                }
                            ]
                        },
                        {
                            "testi3": [
                                {
                                    "fotoTesti": {
                                        "img": "images/xperson_3.jpg.pagespeed.ic.Cln-jaM1jK.webp"
                                    }
                                },
                                {
                                    "bintang": {
                                        "icon": "fa fa-star"
                                    }
                                },
                                {
                                    "isiTesti": {
                                        "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                    }
                                },
                                {
                                    "namaTesti": {
                                        "text": "Roger Scott"
                                    }
                                },
                                {
                                    "position": {
                                        "text": "Cheif Executive Officer @pexman"
                                    }
                                }
                            ]
                        },
                        {
                            "testi4": [
                                {
                                    "fotoTesti": {
                                        "img": "images/xperson_4.jpg.pagespeed.ic.ucbtJ1Htlo.webp"
                                    }
                                },
                                {
                                    "bintang": {
                                        "icon": "fa fa-star"
                                    }
                                },
                                {
                                    "isiTesti": {
                                        "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                    }
                                },
                                {
                                    "namaTesti": {
                                        "text": "Roger Scott"
                                    }
                                },
                                {
                                    "position": {
                                        "text": "Cheif Executive Officer @pexman"
                                    }
                                }
                            ]
                        },
                        {
                            "testi5": [
                                {
                                    "fotoTesti": {
                                        "img": "images/xperson_2.jpg.pagespeed.ic.Xrdu_nPZRp.webp"
                                    }
                                },
                                {
                                    "bintang": {
                                        "icon": "fa fa-star"
                                    }
                                },
                                {
                                    "isiTesti": {
                                        "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                    }
                                },
                                {
                                    "namaTesti": {
                                        "text": "Roger Scott"
                                    }
                                },
                                {
                                    "position": {
                                        "text": "Cheif Executive Officer @pexman"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class home_Read_Latest_News(Resource):
    def get(self):
        return {
            "data": [
                {
                    "Read Latest News": [
                        {
                            "heading": {
                                "subHeading": "READ LATEST NEWS",
                                "textjudul": "Our Latest Blog"
                            }
                        },
                        {
                            "isi Red Latest News": [
                                {
                                    "img": "images/ximage_1.jpg.pagespeed.ic.FL0iBhryhq.webp",
                                    "url": "https://preview.colorlib.com/theme/pexman/blog-single.html",
                                    "icon": "fa fa-calendar",
                                    "textTanggal": "Oct. 27, 2020",
                                    "title": "Far far away, behind the word mountains",
                                    "textIsi": "Far far away, behind the word mountains, far from the countries.",
                                    "urlJudul": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "img": "images/ximage_2.jpg.pagespeed.ic.-x0Ll8ptzk.webp",
                                    "urlimg": "https://preview.colorlib.com/theme/pexman/blog-single.html",
                                    "icon": "fa fa-calendar",
                                    "textTanggal": "Oct. 27, 2020",
                                    "title": "Far far away, behind the word mountains",
                                    "textIsi": "Far far away, behind the word mountains, far from the countries.",
                                    "urlJudul": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "img": "images/ximage_3.jpg.pagespeed.ic.DwkWtPATES.webp",
                                    "urlimg": "https://preview.colorlib.com/theme/pexman/blog-single.html",
                                    "icon": "fa fa-calendar",
                                    "textTanggal": "Oct. 27, 2020",
                                    "title": "Far far away, behind the word mountains",
                                    "textIsi": "Far far away, behind the word mountains, far from the countries.",
                                    "urlJudul": "https://preview.colorlib.com/theme/pexman/#"
                                },
                                {
                                    "img": "images/ximage_4.jpg.pagespeed.ic.r0BKEhAIc3.webp",
                                    "urlimg": "https://preview.colorlib.com/theme/pexman/blog-single.html",
                                    "icon": "fa fa-calendar",
                                    "textTanggal": "Oct. 27, 2020",
                                    "title": "Far far away, behind the word mountains",
                                    "textIsi": "Far far away, behind the word mountains, far from the countries.",
                                    "urlJudul": "https://preview.colorlib.com/theme/pexman/#"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class home_pexman(Resource):
    def get(self):
        return {
            "data": [
                {
                    "Pexman": [
                        {
                            "textJudul": "Pexman",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                        }
                    ]
                }
            ]
        }


class home_ContactUs(Resource):
    def get(self):
        return {
            "data": [
                {
                    "connect With Us": [
                        {
                            "textJudul": "Connect with us"
                        },
                        {
                            "icon": "fa fa-twitter",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "icon": "fa fa-facebook",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "icon": "fa fa-instagram",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        }
                    ]
                }
            ]
        }


class home_navigation(Resource):
    def get(self):
        return {
            "data": [
                {
                    "Navigation": [
                        {
                            "textJudul": "Navigation"
                        },
                        {
                            "text": "Home",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "text": "Work",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "text": "About",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "text": "Blog",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "text": "Press",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "text": "Blog",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "text": "Contact",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "text": "Support",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "text": "Privacy",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        }
                    ]
                }
            ]
        }


class home_question(Resource):
    def get(self):
        return {
            "data": [
                {
                    "Have a Question": [
                        {
                            "textJudul": "Have a Question?"
                        },
                        {
                            "icon": "fa fa-map marker",
                            "text": "203 Fake St. Mountain View, San Francisco, California, USA"
                        },
                        {
                            "icon": "fa fa-phone",
                            "text": "+2 392 3929 210",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "icon": "fa fa-paper-plane",
                            "text": "info@yourdomain.com",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        }
                    ]
                }
            ]
        }


class home_akhir(Resource):
    def get(self):
        return {
            "data": [
                {
                    "akhir": {
                        "text": "Copyright ©2022 All rights reserved | This template is made with  by Colorlib",
                        "url": "https://colorlib.com/",
                        "icon": "fa fa-heart"
                    }
                }
            ]
        }


class about_(Resource):
    def get(self):
        return {
            "data": [
                {
                    "overlay": [
                        {
                            "background": "images/xbg_1.jpg.pagespeed.ic.Ojq-dWQTjg.webp"
                        },
                        {
                            "text": "Home",
                            "url": "https://preview.colorlib.com/theme/pexman/index.html",
                            "icon": "fa fa-chevron-right"
                        },
                        {
                            "text": "About Us",
                            "icon": "fa fa-chevron-right"
                        },
                        {
                            "judulHal": "About Us"
                        }
                    ]
                },
                {
                    "welcome": [
                        {
                            "img": "images/xabout.jpg.pagespeed.ic.8p3LFl59dX.webp"
                        },
                        {
                            "subHeading": {
                                "text": "Welcome Pexman"
                            }
                        },
                        {
                            "subTitle": {
                                "text": "We Are Creative Agency That Create Beautiful Websites"
                            }
                        },
                        {
                            "isikonten": [
                                {
                                    "paraf1": {
                                        "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean."
                                    }
                                },
                                {
                                    "paraf2": {
                                        "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean."
                                    }
                                }
                            ]
                        },
                        {
                            "button": [
                                {
                                    "text": "Start A Project",
                                    "icon": "on ion-ios-arrow-round-forward"
                                }
                            ]
                        }
                    ]
                },
                {
                    "rating": [
                        {
                            "background": {
                                "img": "images/xbg_1.jpg.pagespeed.ic.Ojq-dWQTjg.webp"
                            }
                        },
                        {
                            "isiRating": [
                                {
                                    "number": "10",
                                    "subNumber": "K+",
                                    "text": "ACHIEVEMENTS"
                                },
                                {
                                    "number": "21",
                                    "subNumber": "K+",
                                    "text": "PROJECT COMPLETED"
                                },
                                {
                                    "number": "27",
                                    "text": "YEARS OF EXPERIENCED"
                                },
                                {
                                    "number": "30",
                                    "subNumber": "K+",
                                    "text": "HAPPY CUSTOMERS"
                                }
                            ]
                        }
                    ]
                },
                {
                    "team": [
                        {
                            "subHeading": {
                                "text": "TEAM"
                            }
                        },
                        {
                            "subTitle": {
                                "text": "Expert Team"
                            }
                        },
                        {
                            "team1": [
                                {
                                    "gambar": {
                                        "img": "images/xteam-5.jpg.pagespeed.ic.KNONdnf_Ng.webp"
                                    }
                                },
                                {
                                    "icnSosmed": [
                                        {
                                            "icon": "fa fa-twitter",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        },
                                        {
                                            "icon": "fa fa-facebook",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        },
                                        {
                                            "icon": "fa fa-google",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        },
                                        {
                                            "icon": "fa fa-instagram",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        }
                                    ]
                                },
                                {
                                    "subName": {
                                        "text": "Luis Wilson"
                                    }
                                },
                                {
                                    "subKeahlian": {
                                        "text": "Web Designer"
                                    }
                                }
                            ]
                        },
                        {
                            "team2": [
                                {
                                    "gambar": {
                                        "img": "images/xteam-2.jpg.pagespeed.ic.lVGVM1ZqjP.webp"
                                    }
                                },
                                {
                                    "icnSosmed": [
                                        {
                                            "icon": "fa fa-twitter",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        },
                                        {
                                            "icon": "fa fa-facebook",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        },
                                        {
                                            "icon": "fa fa-google",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        },
                                        {
                                            "icon": "fa fa-instagram",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        }
                                    ]
                                },
                                {
                                    "subName": {
                                        "text": "Jhemon Wills"
                                    }
                                },
                                {
                                    "subKeahlian": {
                                        "text": "Web Developer"
                                    }
                                }
                            ]
                        },
                        {
                            "team3": [
                                {
                                    "gambar": {
                                        "img": "images/xteam-3.jpg.pagespeed.ic.ZduX31RDtO.webp"
                                    }
                                },
                                {
                                    "icnSosmed": [
                                        {
                                            "icon": "fa fa-twitter",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        },
                                        {
                                            "icon": "fa fa-facebook",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        },
                                        {
                                            "icon": "fa fa-google",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        },
                                        {
                                            "icon": "fa fa-instagram",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        }
                                    ]
                                },
                                {
                                    "subName": {
                                        "text": "Claudia Smith"
                                    }
                                },
                                {
                                    "subKeahlian": {
                                        "text": "Marketing Analyst"
                                    }
                                }
                            ]
                        },
                        {
                            "team4": [
                                {
                                    "gambar": {
                                        "img": "images/xteam-4.jpg.pagespeed.ic.awW0IeAxxv.webp"
                                    }
                                },
                                {
                                    "icnSosmed": [
                                        {
                                            "icon": "fa fa-twitter",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        },
                                        {
                                            "icon": "fa fa-facebook",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        },
                                        {
                                            "icon": "fa fa-google",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        },
                                        {
                                            "icon": "fa fa-instagram",
                                            "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                        }
                                    ]
                                },
                                {
                                    "subName": {
                                        "text": "Rebica Henderson"
                                    }
                                },
                                {
                                    "subKeahlian": {
                                        "text": "System Analyst"
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "testimoni": [
                        {
                            "subHeading": {
                                "text": "TESTIMONIAL"
                            }
                        },
                        {
                            "subTitle": {
                                "text": "What Are Clients Says"
                            }
                        },
                        {
                            "testi1": [
                                {
                                    "fotoTesti": {
                                        "img": "images/xperson_1.jpg.pagespeed.ic.a2MnMHMs44.webp"
                                    }
                                },
                                {
                                    "bintang": {
                                        "icon": "fa fa-star"
                                    }
                                },
                                {
                                    "isiTesti": {
                                        "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                    }
                                },
                                {
                                    "namaTesti": {
                                        "text": "Roger Scott"
                                    }
                                },
                                {
                                    "position": {
                                        "text": "Cheif Executive Officer @pexman"
                                    }
                                }
                            ]
                        },
                        {
                            "testi2": [
                                {
                                    "fotoTesti": {
                                        "img": "images/xperson_2.jpg.pagespeed.ic.Xrdu_nPZRp.webp"
                                    }
                                },
                                {
                                    "bintang": {
                                        "icon": "fa fa-star"
                                    }
                                },
                                {
                                    "isiTesti": {
                                        "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                    }
                                },
                                {
                                    "namaTesti": {
                                        "text": "Roger Scott"
                                    }
                                },
                                {
                                    "position": {
                                        "text": "Cheif Executive Officer @pexman"
                                    }
                                }
                            ]
                        },
                        {
                            "testi3": [
                                {
                                    "fotoTesti": {
                                        "img": "images/xperson_3.jpg.pagespeed.ic.Cln-jaM1jK.webp"
                                    }
                                },
                                {
                                    "bintang": {
                                        "icon": "fa fa-star"
                                    }
                                },
                                {
                                    "isiTesti": {
                                        "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                    }
                                },
                                {
                                    "namaTesti": {
                                        "text": "Roger Scott"
                                    }
                                },
                                {
                                    "position": {
                                        "text": "Cheif Executive Officer @pexman"
                                    }
                                }
                            ]
                        },
                        {
                            "testi4": [
                                {
                                    "fotoTesti": {
                                        "img": "images/xperson_4.jpg.pagespeed.ic.ucbtJ1Htlo.webp"
                                    }
                                },
                                {
                                    "bintang": {
                                        "icon": "fa fa-star"
                                    }
                                },
                                {
                                    "isiTesti": {
                                        "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                    }
                                },
                                {
                                    "namaTesti": {
                                        "text": "Roger Scott"
                                    }
                                },
                                {
                                    "position": {
                                        "text": "Cheif Executive Officer @pexman"
                                    }
                                }
                            ]
                        },
                        {
                            "testi5": [
                                {
                                    "fotoTesti": {
                                        "img": "images/xperson_2.jpg.pagespeed.ic.Xrdu_nPZRp.webp"
                                    }
                                },
                                {
                                    "bintang": {
                                        "icon": "fa fa-star"
                                    }
                                },
                                {
                                    "isiTesti": {
                                        "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                    }
                                },
                                {
                                    "namaTesti": {
                                        "text": "Roger Scott"
                                    }
                                },
                                {
                                    "position": {
                                        "text": "Cheif Executive Officer @pexman"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class about_overlay(Resource):
    def get(self):
        return {
            "data": [
                {
                    "overlay": [
                        {
                            "background": "images/xbg_1.jpg.pagespeed.ic.Ojq-dWQTjg.webp"
                        },
                        {
                            "text": "Home",
                            "url": "https://preview.colorlib.com/theme/pexman/index.html",
                            "icon": "fa fa-chevron-right"
                        },
                        {
                            "text": "About Us",
                            "icon": "fa fa-chevron-right"
                        },
                        {
                            "judulHal": "About Us"
                        }
                    ]
                }
            ]
        }


class about_welcome(Resource):
    def get(self):
        return {
            "data": {
                "welcome": [
                    {
                        "img": "images/xabout.jpg.pagespeed.ic.8p3LFl59dX.webp"
                    },
                    {
                        "subHeading": {
                            "text": "Welcome Pexman"
                        }
                    },
                    {
                        "subTitle": {
                            "text": "We Are Creative Agency That Create Beautiful Websites"
                        }
                    },
                    {
                        "isikonten": [
                            {
                                "paraf1": {
                                    "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean."
                                }
                            },
                            {
                                "paraf2": {
                                    "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean."
                                }
                            }
                        ]
                    },
                    {
                        "button": [
                            {
                                "text": "Start A Project",
                                "icon": "on ion-ios-arrow-round-forward"
                            }
                        ]
                    }
                ]
            }
        }


class about_rating(Resource):
    def get(self):
        return {
            "data": {
                "rating": [
                    {
                        "background": {
                            "img": "images/xbg_1.jpg.pagespeed.ic.Ojq-dWQTjg.webp"
                        }
                    },
                    {
                        "isiRating": [
                            {
                                "number": "10",
                                "subNumber": "K+",
                                "text": "ACHIEVEMENTS"
                            },
                            {
                                "number": "21",
                                "subNumber": "K+",
                                "text": "PROJECT COMPLETED"
                            },
                            {
                                "number": "27",
                                "text": "YEARS OF EXPERIENCED"
                            },
                            {
                                "number": "30",
                                "subNumber": "K+",
                                "text": "HAPPY CUSTOMERS"
                            }
                        ]
                    }
                ]
            }
        }


class about_tim(Resource):
    def get(self):
        return {
            "data": {
                "team": [
                    {
                        "subHeading": {
                            "text": "TEAM"
                        }
                    },
                    {
                        "subTitle": {
                            "text": "Expert Team"
                        }
                    },
                    {
                        "team1": [
                            {
                                "gambar": {
                                    "img": "images/xteam-5.jpg.pagespeed.ic.KNONdnf_Ng.webp"
                                }
                            },
                            {
                                "icnSosmed": [
                                    {
                                        "icon": "fa fa-twitter",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    },
                                    {
                                        "icon": "fa fa-facebook",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    },
                                    {
                                        "icon": "fa fa-google",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    },
                                    {
                                        "icon": "fa fa-instagram",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    }
                                ]
                            },
                            {
                                "subName": {
                                    "text": "Luis Wilson"
                                }
                            },
                            {
                                "subKeahlian": {
                                    "text": "Web Designer"
                                }
                            }
                        ]
                    },
                    {
                        "team2": [
                            {
                                "gambar": {
                                    "img": "images/xteam-2.jpg.pagespeed.ic.lVGVM1ZqjP.webp"
                                }
                            },
                            {
                                "icnSosmed": [
                                    {
                                        "icon": "fa fa-twitter",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    },
                                    {
                                        "icon": "fa fa-facebook",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    },
                                    {
                                        "icon": "fa fa-google",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    },
                                    {
                                        "icon": "fa fa-instagram",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    }
                                ]
                            },
                            {
                                "subName": {
                                    "text": "Jhemon Wills"
                                }
                            },
                            {
                                "subKeahlian": {
                                    "text": "Web Developer"
                                }
                            }
                        ]
                    },
                    {
                        "team3": [
                            {
                                "gambar": {
                                    "img": "images/xteam-3.jpg.pagespeed.ic.ZduX31RDtO.webp"
                                }
                            },
                            {
                                "icnSosmed": [
                                    {
                                        "icon": "fa fa-twitter",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    },
                                    {
                                        "icon": "fa fa-facebook",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    },
                                    {
                                        "icon": "fa fa-google",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    },
                                    {
                                        "icon": "fa fa-instagram",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    }
                                ]
                            },
                            {
                                "subName": {
                                    "text": "Claudia Smith"
                                }
                            },
                            {
                                "subKeahlian": {
                                    "text": "Marketing Analyst"
                                }
                            }
                        ]
                    },
                    {
                        "team4": [
                            {
                                "gambar": {
                                    "img": "images/xteam-4.jpg.pagespeed.ic.awW0IeAxxv.webp"
                                }
                            },
                            {
                                "icnSosmed": [
                                    {
                                        "icon": "fa fa-twitter",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    },
                                    {
                                        "icon": "fa fa-facebook",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    },
                                    {
                                        "icon": "fa fa-google",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    },
                                    {
                                        "icon": "fa fa-instagram",
                                        "url": "https://preview.colorlib.com/theme/pexman/about.html#"
                                    }
                                ]
                            },
                            {
                                "subName": {
                                    "text": "Rebica Henderson"
                                }
                            },
                            {
                                "subKeahlian": {
                                    "text": "System Analyst"
                                }
                            }
                        ]
                    }
                ]
            }
        }


class about_testimoni(Resource):
    def get(self):
        return {
            "data": {
                "testimoni": [
                    {
                        "subHeading": {
                            "text": "TESTIMONIAL"
                        }
                    },
                    {
                        "subTitle": {
                            "text": "What Are Clients Says"
                        }
                    },
                    {
                        "testi1": [
                            {
                                "fotoTesti": {
                                    "img": "images/xperson_1.jpg.pagespeed.ic.a2MnMHMs44.webp"
                                }
                            },
                            {
                                "bintang": {
                                    "icon": "fa fa-star"
                                }
                            },
                            {
                                "isiTesti": {
                                    "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                }
                            },
                            {
                                "namaTesti": {
                                    "text": "Roger Scott"
                                }
                            },
                            {
                                "position": {
                                    "text": "Cheif Executive Officer @pexman"
                                }
                            }
                        ]
                    },
                    {
                        "testi2": [
                            {
                                "fotoTesti": {
                                    "img": "images/xperson_2.jpg.pagespeed.ic.Xrdu_nPZRp.webp"
                                }
                            },
                            {
                                "bintang": {
                                    "icon": "fa fa-star"
                                }
                            },
                            {
                                "isiTesti": {
                                    "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                }
                            },
                            {
                                "namaTesti": {
                                    "text": "Roger Scott"
                                }
                            },
                            {
                                "position": {
                                    "text": "Cheif Executive Officer @pexman"
                                }
                            }
                        ]
                    },
                    {
                        "testi3": [
                            {
                                "fotoTesti": {
                                    "img": "images/xperson_3.jpg.pagespeed.ic.Cln-jaM1jK.webp"
                                }
                            },
                            {
                                "bintang": {
                                    "icon": "fa fa-star"
                                }
                            },
                            {
                                "isiTesti": {
                                    "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                }
                            },
                            {
                                "namaTesti": {
                                    "text": "Roger Scott"
                                }
                            },
                            {
                                "position": {
                                    "text": "Cheif Executive Officer @pexman"
                                }
                            }
                        ]
                    },
                    {
                        "testi4": [
                            {
                                "fotoTesti": {
                                    "img": "images/xperson_4.jpg.pagespeed.ic.ucbtJ1Htlo.webp"
                                }
                            },
                            {
                                "bintang": {
                                    "icon": "fa fa-star"
                                }
                            },
                            {
                                "isiTesti": {
                                    "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                }
                            },
                            {
                                "namaTesti": {
                                    "text": "Roger Scott"
                                }
                            },
                            {
                                "position": {
                                    "text": "Cheif Executive Officer @pexman"
                                }
                            }
                        ]
                    },
                    {
                        "testi5": [
                            {
                                "fotoTesti": {
                                    "img": "images/xperson_2.jpg.pagespeed.ic.Xrdu_nPZRp.webp"
                                }
                            },
                            {
                                "bintang": {
                                    "icon": "fa fa-star"
                                }
                            },
                            {
                                "isiTesti": {
                                    "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
                                }
                            },
                            {
                                "namaTesti": {
                                    "text": "Roger Scott"
                                }
                            },
                            {
                                "position": {
                                    "text": "Cheif Executive Officer @pexman"
                                }
                            }
                        ]
                    }
                ]
            }
        }


class portofolio(Resource):
    def get(self):
        return {
            "data": [
                {
                    "overlay": [
                        {
                            "background": "images/xbg_1.jpg.pagespeed.ic.Ojq-dWQTjg.webp"
                        },
                        {
                            "text": "Home",
                            "url": "https://preview.colorlib.com/theme/pexman/index.html",
                            "icon": "fa fa-chevron-right"
                        },
                        {
                            "text": "PORTOFOLIO",
                            "icon": "fa fa-chevron-right"
                        },
                        {
                            "judulHal": {
                                "text": "PORTOFOLIO"
                            }
                        }
                    ]
                },
                {
                    "menuPorto": [
                        {
                            "text": "ALL",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "text": "BRANDING",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "text": "WEB DESIGN",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "text": "ILLUSTRATION",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        },
                        {
                            "text": "APPLICATION",
                            "url": "https://preview.colorlib.com/theme/pexman/#"
                        }
                    ]
                },
                {
                    "isiportofolio": [
                        {
                            "img": "images/xwork-1.jpg.pagespeed.ic.3j7JGYqbGF.webp",
                            "judul": "Hark Website",
                            "subJudul": "WEB DESIGN,BRANDING",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                            "icon": "fa fa-search"
                        },
                        {
                            "img": "images/xwork-2.jpg.pagespeed.ic.10n42M66q2.webp",
                            "judul": "Hark Website",
                            "subJudul": "WEB DESIGN,BRANDING",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                            "icon": "fa fa-search"
                        },
                        {
                            "img": "images/xwork-3.jpg.pagespeed.ic.RnZ9RkAZUD.webp",
                            "judul": "Hark Website",
                            "subJudul": "WEB DESIGN,BRANDING",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                            "icon": "fa fa-search"
                        },
                        {
                            "img": "images/xwork-4.jpg.pagespeed.ic.RrfN8RD85H.webp",
                            "judul": "Hark Website",
                            "subJudul": "WEB DESIGN,BRANDING",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                            "icon": "fa fa-search"
                        },
                        {
                            "img": "images/xwork-5.jpg.pagespeed.ic.tS4bFn-pmq.webp",
                            "judul": "Hark Website",
                            "subJudul": "WEB DESIGN,BRANDING",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                            "icon": "fa fa-search"
                        },
                        {
                            "img": "images/xwork-6.jpg.pagespeed.ic.RupLEjxNLP.webp",
                            "judul": "Hark Website",
                            "subJudul": "WEB DESIGN,BRANDING",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                            "icon": "fa fa-search"
                        },
                        {
                            "img": "images/xwork-7.jpg.pagespeed.ic.VL2SUY_RpS.webp",
                            "judul": "Hark Website",
                            "subJudul": "WEB DESIGN,BRANDING",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                            "icon": "fa fa-search"
                        },
                        {
                            "img": "images/xwork-8.jpg.pagespeed.ic.BEEvFj7ItC.webp",
                            "judul": "Hark Website",
                            "subJudul": "WEB DESIGN,BRANDING",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                            "icon": "fa fa-search"
                        },
                        {
                            "img": "(images/work-9.jpg",
                            "judul": "Hark Website",
                            "subJudul": "WEB DESIGN,BRANDING",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                            "icon": "fa fa-search"
                        },
                        {
                            "img": "images/work-10.jpg",
                            "judul": "Hark Website",
                            "subJudul": "WEB DESIGN,BRANDING",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                            "icon": "fa fa-search"
                        },
                        {
                            "img": "images/work-11.jpg",
                            "judul": "Hark Website",
                            "subJudul": "WEB DESIGN,BRANDING",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                            "icon": "fa fa-search"
                        },
                        {
                            "img": "images/work-12.jpg",
                            "judul": "Hark Website",
                            "subJudul": "WEB DESIGN,BRANDING",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html",
                            "icon": "fa fa-search"
                        }
                    ]
                },
                {
                    "slideAngka": [
                        {
                            "text": "&lt;",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html#"
                        },
                        {
                            "text": "1",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html#"
                        },
                        {
                            "text": "2",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html#"
                        },
                        {
                            "text": "3",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html#"
                        },
                        {
                            "text": "4",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html#"
                        },
                        {
                            "text": "5",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html#"
                        },
                        {
                            "text": "&gt",
                            "url": "https://preview.colorlib.com/theme/pexman/work.html#"
                        }
                    ]
                }
            ]
        }


class portoforlio_overlay(Resource):
    def get(self):
        return {
            "data": {
                "overlay": [
                    {
                        "background": "images/xbg_1.jpg.pagespeed.ic.Ojq-dWQTjg.webp"
                    },
                    {
                        "text": "Home",
                        "url": "https://preview.colorlib.com/theme/pexman/index.html",
                        "icon": "fa fa-chevron-right"
                    },
                    {
                        "text": "PORTOFOLIO",
                        "icon": "fa fa-chevron-right"
                    },
                    {
                        "judulHal": {
                            "text": "PORTOFOLIO"
                        }
                    }
                ]
            }
        }


class portofolio_Menu(Resource):
    def get(self):
        return {
            "data": {
                "menuPorto": [
                    {
                        "text": "ALL",
                        "url": "https://preview.colorlib.com/theme/pexman/#"
                    },
                    {
                        "text": "BRANDING",
                        "url": "https://preview.colorlib.com/theme/pexman/#"
                    },
                    {
                        "text": "WEB DESIGN",
                        "url": "https://preview.colorlib.com/theme/pexman/#"
                    },
                    {
                        "text": "ILLUSTRATION",
                        "url": "https://preview.colorlib.com/theme/pexman/#"
                    },
                    {
                        "text": "APPLICATION",
                        "url": "https://preview.colorlib.com/theme/pexman/#"
                    }
                ]
            }
        }


class portofolio_isi(Resource):
    def get(self):
        return {
            "data": {
                "isiportofolio": [
                    {
                        "img": "images/xwork-1.jpg.pagespeed.ic.3j7JGYqbGF.webp",
                        "judul": "Hark Website",
                        "subJudul": "WEB DESIGN,BRANDING",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html",
                        "icon": "fa fa-search"
                    },
                    {
                        "img": "images/xwork-2.jpg.pagespeed.ic.10n42M66q2.webp",
                        "judul": "Hark Website",
                        "subJudul": "WEB DESIGN,BRANDING",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html",
                        "icon": "fa fa-search"
                    },
                    {
                        "img": "images/xwork-3.jpg.pagespeed.ic.RnZ9RkAZUD.webp",
                        "judul": "Hark Website",
                        "subJudul": "WEB DESIGN,BRANDING",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html",
                        "icon": "fa fa-search"
                    },
                    {
                        "img": "images/xwork-4.jpg.pagespeed.ic.RrfN8RD85H.webp",
                        "judul": "Hark Website",
                        "subJudul": "WEB DESIGN,BRANDING",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html",
                        "icon": "fa fa-search"
                    },
                    {
                        "img": "images/xwork-5.jpg.pagespeed.ic.tS4bFn-pmq.webp",
                        "judul": "Hark Website",
                        "subJudul": "WEB DESIGN,BRANDING",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html",
                        "icon": "fa fa-search"
                    },
                    {
                        "img": "images/xwork-6.jpg.pagespeed.ic.RupLEjxNLP.webp",
                        "judul": "Hark Website",
                        "subJudul": "WEB DESIGN,BRANDING",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html",
                        "icon": "fa fa-search"
                    },
                    {
                        "img": "images/xwork-7.jpg.pagespeed.ic.VL2SUY_RpS.webp",
                        "judul": "Hark Website",
                        "subJudul": "WEB DESIGN,BRANDING",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html",
                        "icon": "fa fa-search"
                    },
                    {
                        "img": "images/xwork-8.jpg.pagespeed.ic.BEEvFj7ItC.webp",
                        "judul": "Hark Website",
                        "subJudul": "WEB DESIGN,BRANDING",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html",
                        "icon": "fa fa-search"
                    },
                    {
                        "img": "(images/work-9.jpg",
                        "judul": "Hark Website",
                        "subJudul": "WEB DESIGN,BRANDING",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html",
                        "icon": "fa fa-search"
                    },
                    {
                        "img": "images/work-10.jpg",
                        "judul": "Hark Website",
                        "subJudul": "WEB DESIGN,BRANDING",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html",
                        "icon": "fa fa-search"
                    },
                    {
                        "img": "images/work-11.jpg",
                        "judul": "Hark Website",
                        "subJudul": "WEB DESIGN,BRANDING",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html",
                        "icon": "fa fa-search"
                    },
                    {
                        "img": "images/work-12.jpg",
                        "judul": "Hark Website",
                        "subJudul": "WEB DESIGN,BRANDING",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html",
                        "icon": "fa fa-search"
                    }
                ]
            }
        }


class portofolio_slide(Resource):
    def get(self):
        return {
            "data": {
                "slideAngka": [
                    {
                        "text": "&lt;",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html#"
                    },
                    {
                        "text": "1",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html#"
                    },
                    {
                        "text": "2",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html#"
                    },
                    {
                        "text": "3",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html#"
                    },
                    {
                        "text": "4",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html#"
                    },
                    {
                        "text": "5",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html#"
                    },
                    {
                        "text": "&gt",
                        "url": "https://preview.colorlib.com/theme/pexman/work.html#"
                    }
                ]
            }
        }


api.add_resource(home_, '/home/'),
api.add_resource(home_navbar, '/home/navbar/'),
api.add_resource(home_carousel, '/home/carousel/'),
api.add_resource(home_welcome, '/home/welcome/'),
api.add_resource(home_rating, '/home/rating/'),
api.add_resource(home_What_We_Offer, '/home/offer/'),
api.add_resource(home_Our_Portofolio, '/home/portofolio/'),
api.add_resource(home_testimoni, '/home/testimoni/'),
api.add_resource(home_Read_Latest_News, '/home/news/'),
api.add_resource(home_pexman, '/home/pexman/'),
api.add_resource(home_ContactUs, '/home/contactUs/'),
api.add_resource(home_navigation, '/home/navigation/'),
api.add_resource(home_question, '/home/nquestion/'),
api.add_resource(home_akhir, '/home/akhir/'),
api.add_resource(about_, '/about/'),
api.add_resource(about_overlay, '/about/overlay/'),
api.add_resource(about_welcome, '/about/welcome/'),
api.add_resource(about_rating, '/about/rating/'),
api.add_resource(about_tim, '/about/tim/'),
api.add_resource(about_testimoni, '/about/testimoni/'),
api.add_resource(portofolio, '/portofolio/'),
api.add_resource(portoforlio_overlay, '/portofolio/overlay/'),
api.add_resource(portofolio_Menu, '/portofolio/menu/'),
api.add_resource(portofolio_isi, '/portofolio/isi/'),
api.add_resource(portofolio_slide, '/portofolio/slide/')


@ app.errorhandler(404)
def page_not_found(e):
    return {"error": "not found end point"}, 404


if __name__ == '__main__':
    app.run(debug=True)
