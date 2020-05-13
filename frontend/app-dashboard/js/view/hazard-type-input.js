define([
    'backbone',
    'js/model/hazard_type.js',], function (Backbone, HazardTypeCollection) {
    return Backbone.View.extend({
        initialize: function ($form) {
            this.$form = $form
            let $el = $form.find('select[name$="hazard_type"]');
            this.$el = $el

            this.collection = new HazardTypeCollection()
            this.collection.fetch().then(function (data) {
                data.forEach(function (value) {
                    $el.append(`<option value="${value.id}">${value.name}</option>`)
                });
            }).catch(function (data) {
                console.log('Hazard type request failed');
                console.log(data);
            });
        },
    });
});
