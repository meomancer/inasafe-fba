-- FLOOD CLASS --
INSERT INTO public.hazard_class (id, label, hazard_type) VALUES (1, 'Class 1: 0 - 0.7m', 1) ON CONFLICT DO NOTHING ;
INSERT INTO public.hazard_class (id, label, hazard_type) VALUES (2, 'Class 2: 0.7 - 1.5m', 1) ON CONFLICT DO NOTHING ;
INSERT INTO public.hazard_class (id, label, hazard_type) VALUES (3, 'Class 3: 1.5 - 3.0m', 1) ON CONFLICT DO NOTHING ;
INSERT INTO public.hazard_class (id, label, hazard_type) VALUES (4, 'Class 4: 3 or greater', 1) ON CONFLICT DO NOTHING ;

-- HURRICANE CLASS : https://www.nhc.noaa.gov/aboutsshws.php--
INSERT INTO public.hazard_class (id, label, hazard_type) VALUES (5, 'Class 1: 74-95 mph', 2) ON CONFLICT DO NOTHING ;
INSERT INTO public.hazard_class (id, label, hazard_type) VALUES (6, 'Class 2: 96-110 mph', 2) ON CONFLICT DO NOTHING ;
INSERT INTO public.hazard_class (id, label, hazard_type) VALUES (7, 'Class 3: 111-129 mph', 2) ON CONFLICT DO NOTHING ;
INSERT INTO public.hazard_class (id, label, hazard_type) VALUES (8, 'Class 4: 130-156 mph', 2) ON CONFLICT DO NOTHING ;
INSERT INTO public.hazard_class (id, label, hazard_type) VALUES (9, 'Class 5: 157 mph or higher', 2) ON CONFLICT DO NOTHING ;