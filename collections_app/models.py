from django.db import models


class Collection(models.Model):
    coll_name = models.CharField('Name',
                                 max_length=255,
                                 blank=False,
                                 default='General Collection',
                                 help_text='Use "General Collection" if describing all files as one '
                                           'combined entry; otherwise, create a separate entry '
                                           'for each formally named collection or collection '
                                           'with special characteristics, for example "The Nettie '
                                           'Wheeler Artist Files on Native American Artists."')
    coll_description = models.TextField('Description',
                                        max_length=1000,
                                        blank=False,
                                        help_text='Provide a general description of the collection, '
                                                  'including such aspects as history and provenance. Also '
                                                  'use this field for general notes about '
                                                  'the collection.')
    coll_access = models.TextField('Access and Use',
                                   max_length=1000,
                                   blank=False,
                                   help_text='Add policies and procedures relating to how '
                                             'researchers access and use the collection.')
    coll_website = models.URLField('Website',
                                   max_length=255,
                                   blank=True,
                                   help_text='Add website describing or providing access to the collection.')
    coll_services = models.ManyToManyField(to='CollectionService',
                                           related_name='Collection',
                                           verbose_name=u'Reference Services',
                                           blank=False,
                                           help_text='Add reference services offered. Create a new service '
                                                     'if there is not a fit.')
    coll_cat_system = models.ManyToManyField(to='CollectionCatSystem',
                                             related_name='Collection',
                                             verbose_name=u'Cataloging Systems',
                                             blank=False,
                                             help_text='Add systems used for cataloging artist files '
                                                       'collection. Create a new system if there is '
                                                       'not a fit.')
    coll_size = models.TextField('Size',
                                 max_length=1000,
                                 default='',
                                 blank=False,
                                 help_text='Provide a statement about the size of the collection, '
                                           'including growth rate, etc. Use whatever measurement terms are '
                                           'relevant.')
    coll_spec_format = models.ManyToManyField(to='CollectionSpecialFormat',
                                              related_name='Collection',
                                              verbose_name=u'Special Formats',
                                              blank=True,
                                              help_text='Add special formats contained in the '
                                                        'collection, either analog or digital. Create a new '
                                                        'type if there is not a fit.')
    coll_dig_projects = models.TextField('Digital Projects',
                                         max_length=1000,
                                         blank=True,
                                         help_text='Describe digital projects, either completed '
                                                   'or planned, for this collection.')
    coll_dig_access = models.URLField('Digital Project Website',
                                      max_length=255,
                                      blank=True,
                                      help_text='Provide URL for accessing digital collection.')
    # Need to work on way for user to choose a featured image below
    coll_image = models.ForeignKey('CollectionImage',
                                   verbose_name=u'Collection Images',
                                   on_delete=models.CASCADE,
                                   blank=True,
                                   null=True,
                                   help_text='Upload images showing example material from files '
                                             'and/or storage systems in use.')
    coll_subject_name = models.ManyToManyField(to='CollectionSubjectName',
                                               related_name='Collection',
                                               verbose_name=u'Subject: Names',
                                               blank=True,
                                               help_text='Add personal and institutional names that '
                                                         'are subjects of the collection.')
    coll_subject_topic = models.ManyToManyField(to='CollectionSubjectTopic',
                                                related_name='Collection',
                                                verbose_name=u'Subject: Topics',
                                                blank=True,
                                                help_text='Add topical terms that are the subject focuses '
                                                          'of the files.')
    coll_subject_city = models.ManyToManyField(to='CollectionSubjectCity',
                                               related_name='Collection',
                                               verbose_name=u'Subject: Cities',
                                               blank=True,
                                               help_text='Add cities that are subject focuses of the files')
    coll_subject_county = models.ManyToManyField(to='CollectionSubjectCounty',
                                                 related_name='Collection',
                                                 verbose_name=u'Subject: Counties',
                                                 blank=True,
                                                 help_text='Add counties that are subject focuses of the '
                                                           'files.')
    coll_subject_state_prov = models.ManyToManyField(to='CollectionSubjectStateProv',
                                                     related_name='Collection',
                                                     verbose_name=u'Subject: States and '
                                                                  'Provinces',
                                                     blank=True,
                                                     help_text='Add states or provinces that are subject '
                                                               'focuses of the files.')
    coll_subject_country = models.ManyToManyField(to='CollectionSubjectCountry',
                                                  related_name='Collection',
                                                  verbose_name=u'Subject: Countries',
                                                  blank=True,
                                                  help_text='Add countries that are subject focuses of the '
                                                            'files.')
    coll_subject_geo_area = models.ManyToManyField(to='CollectionSubjectGeoArea',
                                                   related_name='Collection',
                                                   verbose_name=u'Subject: Geographic Areas',
                                                   blank=True,
                                                   help_text='Add geographic areas, such as "West U.S." that '
                                                             'are subject focuses of the files.')

    # Need to develop a way, function, etc, for entering city then automatically filling in higher
    # geographical hierarchies, including zip
    coll_loc_city = models.CharField('Location: City',
                                     max_length=255,
                                     help_text='Important for providing access to collections located in '
                                               'specific cities.',
                                     blank=False)
    coll_loc_state_prov = models.CharField('Location: State/Province',
                                           max_length=255,
                                           help_text='Important for providing access to collections located'
                                                     ' in specific states or provinces.',
                                           blank=False)
    coll_loc_country = models.CharField('Location: Country',
                                        max_length=255,
                                        help_text='Important for providing access to collections located in '
                                                  'specific countries.',
                                        blank=False)
    coll_date_created = models.DateField(auto_now_add=True)
    coll_date_saved = models.DateField(auto_now=True)

    def __str__(self):
        return self.coll_name

    class Meta:
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'
        ordering = ['coll_name']


class CollectionService(models.Model):
    coll_serv_name = models.CharField('Reference Service',
                                      max_length=100,
                                      blank=False,
                                      help_text='')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_serv_name

    class Meta:
        verbose_name = 'Reference Service'
        verbose_name_plural = 'Reference Services'
        ordering = ['coll_serv_name']


class CollectionCatSystem(models.Model):
    coll_cat_name = models.CharField('Cataloging System',
                                     max_length=100,
                                     help_text='')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_cat_name

    class Meta:
        verbose_name = 'Cataloging System'
        verbose_name_plural = 'Cataloging Systems'
        ordering = ['coll_cat_name']


class CollectionSpecialFormat(models.Model):
    # Use id.loc.gov
    coll_special_format = models.CharField('Special Format',
                                           max_length=100,
                                           help_text='')
    coll_special_format_url = models.URLField('Term Reference',
                                              max_length=255,
                                              help_text='Provide URI from <a '
                                                        'href="http://id.loc.gov/vocabulary'
                                                        '/graphicMaterials.html" '
                                                        'target="_blank">Thesaurus for Graphic '
                                                        'Materials</a>, '
                                                        '<a '
                                                        'href="http://id.loc.gov/authorities/genreForms'
                                                        '.html" '
                                                        'target="_blank">Library of Congress Genre/Form '
                                                        'Terms</a>, '
                                                        '<a href="http://www.wikipedia.org" '
                                                        'target="_blank">Wikipedia</a> URL, '
                                                        'or other URL.',
                                              blank=True)
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_special_format

    class Meta:
        verbose_name = 'Special Format'
        verbose_name_plural = 'Special Formats'
        ordering = ['coll_special_format']


class CollectionImage(models.Model):
    coll_image = models.ImageField('Add Image',
                                   upload_to='collection/images/',
                                   help_text='Upload images showing example material from files '
                                             'and/or storage systems in use.')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class CollectionSubjectName(models.Model):
    # Use VIAF
    coll_sub_name = models.CharField('Subject: Name',
                                     max_length=100,
                                     blank="False",
                                     help_text='Use preferred <a '
                                               'href="http://www.viaf.org" '
                                               'target="_blank">VIAF</a> form '
                                               'of '
                                               'name.')
    coll_sub_name_url = models.URLField('Form of Name Reference',
                                        max_length=255,
                                        help_text='Provide <a href="http://www.viaf.org" '
                                                  'target="_blank">VIAF</a> permalink.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_sub_name

    class Meta:
        verbose_name = 'Subject: Name'
        verbose_name_plural = 'Subject: Names'
        ordering = ['coll_sub_name']


class CollectionSubjectTopic(models.Model):
    # Use id.loc.gov?
    coll_sub_topic = models.CharField('Subject: Topic',
                                      max_length=100,
                                      blank=False,
                                      help_text='Use term from <a '
                                                'href="http://id.loc.gov/authorities/subjects.html" '
                                                'target="_blank">Library of Congress Subject Headings '
                                                '</a> or other authority.')
    coll_sub_topic_url = models.URLField('Term Reference',
                                         max_length=255,
                                         help_text='Provide URI to term.',
                                         default='',
                                         blank=True)
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_sub_topic

    class Meta:
        verbose_name = 'Subject: Topic'
        verbose_name_plural = 'Subject: Topics'
        ordering = ['coll_sub_topic']


class CollectionSubjectCity(models.Model):
    # use VIAF
    coll_sub_city = models.CharField('Subject: City',
                                     max_length=100,
                                     blank=False,
                                     help_text='Use term from <a '
                                               'href="http://id.loc.gov/authorities/subjects.html" '
                                               'target="_blank">Library of Congress Subject Headings</a> '
                                               'or other authority.')
    coll_sub_city_url = models.URLField('Term Reference',
                                        max_length=255,
                                        help_text='Provide URI to term.',
                                        default='',
                                        blank=True)
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_sub_city

    class Meta:
        verbose_name = 'Subject: City'
        verbose_name_plural = 'Subject: Cities'
        ordering = ['coll_sub_city']


class CollectionSubjectCounty(models.Model):
    # use VIAF
    coll_sub_county = models.CharField('Subject: County',
                                       max_length=100,
                                       blank=False,
                                       help_text='Use term from <a '
                                                 'href="http://id.loc.gov/authorities/subjects.html" '
                                                 'target="_blank">Library of Congress Subject Headings '
                                                 '</a> or other authority.')
    coll_sub_county_url = models.URLField('Term Reference',
                                          max_length=255,
                                          blank=True,
                                          help_text='Provide URI to term.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_sub_county

    class Meta:
        verbose_name = 'Subject: County'
        verbose_name_plural = 'Subject: Counties'
        ordering = ['coll_sub_county']


class CollectionSubjectStateProv(models.Model):
    # Use VIAF
    coll_sub_state_prov = models.CharField('Subject: State/Province',
                                           max_length=100,
                                           blank=False,
                                           help_text='Use term from <a '
                                                     'href="http://id.loc.gov/authorities/subjects.html'
                                                     '" target="_blank">Library of Congress Subject '
                                                     'Headings</a> or other authority.')
    coll_sub_state_prov_url = models.URLField('Term Reference',
                                              max_length=255,
                                              blank=True,
                                              help_text='Provide URI to term.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_sub_state_prov

    class Meta:
        verbose_name = 'Subject: State/Province'
        verbose_name_plural = 'Subject: State/Provinces '
        ordering = ['coll_sub_state_prov']


class CollectionSubjectCountry(models.Model):
    # Use VIAF
    coll_sub_country = models.CharField('Subject: Country',
                                        max_length=100,
                                        blank=False,
                                        help_text='Use term from <a '
                                                  'href="http://id.loc.gov/authorities/subjects.html" '
                                                  'target="_blank">Library of Congress Subject Headings '
                                                  '</a> or other authority.')
    coll_sub_country_url = models.URLField('Term Reference',
                                           max_length=255,
                                           help_text='Provide URI to term.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_sub_country

    class Meta:
        verbose_name = 'Subject: Country'
        verbose_name_plural = 'Subject: Countries'
        ordering = ['coll_sub_country']


class CollectionSubjectGeoArea(models.Model):
    # use VIAF
    coll_sub_geo_area = models.CharField('Subject: Geographic Area',
                                         max_length=100,
                                         blank=False,
                                         help_text='Use term from <a '
                                                   'href="http://id.loc.gov/authorities/subjects.html" '
                                                   'target="_blank">Library of Congress Subject Headings '
                                                   '</a> or other authority.')
    coll_sub_geo_area_url = models.URLField('Term Reference',
                                            max_length=255,
                                            blank=True,
                                            help_text='Provide URI to term.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_sub_geo_area

    class Meta:
        verbose_name = 'Subject: Geographic Area'
        verbose_name_plural = 'Subject: Geographic Areas'
        ordering = ['coll_sub_geo_area']


class CollectionLanguage(models.Model):
    # use id.loc.gov?
    coll_lang = models.CharField('Language',
                                 max_length=100,
                                 blank=False,
                                 help_text='Use language term from <a '
                                           'href="http://id.loc.gov/vocabulary/languages.html" '
                                           'target="_blank">MARC List '
                                           'for Languages</a> or other authority.')
    coll_lang_url = models.URLField('Language Name Reference',
                                    max_length=255,
                                    blank=True,
                                    help_text='Provide URI to term.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_lang

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        ordering = ['coll_lang']
