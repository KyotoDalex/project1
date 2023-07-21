  <div class="tab-pane " id="yamal2" aria-labelledby="yamal2-tab">
                             {% for yamal_post in yamal_posts %}
                                <div class="vs-blog vs-blog-wide bg-secondary mb-20">
                                    <div class="vs-blog-image image-scale-hover">
                                        <a href="post.html"><img src="../static/assets/img/more-news/more-news-1-4.jpg" alt="More News image" class="w-100"></a>
                                    </div>
                                    <div class="vs-blog-content">
                                        <h3 class="blog-title text-medium h4 mb-2"><a href="{{ yamal_post.url }}">{{ yamal_post.title |richtext}}</a></h3>
                                        <div class="blog-meta mb-10">
                                            <a href="{{ yamal_post.url }}"><i class="fal fa-calendar-alt"></i>Dec 20, 2020</a>
                                        </div>
                                          {% for block in yamal_post.body %}
                                                {% if forloop.counter0 < 3 %}
                                                    {% if block.block_type == 'Text' %}

                                                     <p>{{ block.value| richtext}}</p>
                                                    {% endif %}
                                                {% endif %}
                                            {% endfor %}
                                        <a href="post.html" class="link-btn">Читать далее<i class="far fa-angle-right"></i></a>
                                    </div>
                                </div>
                                <div class="text-center pt-10 mb-30">
                                    <a href="#" class="vs-btn">Загрузить далее...</a>
                                </div>
                            </div>
                        {% endfor %}

                            <div class="tab-pane " id="tyumen2" aria-labelledby="tyumen2-tab">
                             {% for tyumen_post in tyumen_posts %}
                                <div class="vs-blog vs-blog-wide bg-secondary mb-20">
                                    <div class="vs-blog-image image-scale-hover">
                                        <a href="{{ tyumen_post.url }}"><img src="../static/assets/img/more-news/more-news-1-9.jpg" alt="More News image" class="w-100"></a>
                                        <div class="blog-category">
                                            <a href="post.html">Путешествия</a>
                                        </div>
                                    </div>
                                    <div class="vs-blog-content">
                                        <h3 class="blog-title text-medium h4 mb-2"><a href="post.html">{{ tyumen_post.title }}</a></h3>
                                        <div class="blog-meta mb-10">
                                            <a href="post.html"><i class="fal fa-user"></i>David Smith</a>
                                            <a href="post.html"><i class="fal fa-calendar-alt"></i>Dec 20, 2020</a>
                                        </div>
                                           {% for block in tyumen_post.body %}
                                                {% if forloop.counter0 < 3 %}
                                                    {% if block.block_type == 'Text' %}

                                                     <p>{{ block.value| richtext}}</p>
                                                    {% endif %}
                                                {% endif %}
                                            {% endfor %}
                                        <a href="post.html" class="link-btn">Читать далее<i class="far fa-angle-right"></i></a>
                                    </div>
                                </div>
                                <div class="text-center pt-10 mb-30">
                                    <a href="#" class="vs-btn">Загрузить далее...</a>
                                </div>
                                {% endfor %}
                            </div>
